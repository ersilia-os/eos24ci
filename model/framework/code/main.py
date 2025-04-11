import pandas as pd
import drugtax
import sys
from rdkit import Chem
import concurrent.futures
from tqdm import tqdm
import os

def kekulize_smiles(smile):
    """Convert a SMILES string to its kekulized form."""
    try:
        m = Chem.MolFromSmiles(smile)
        if m is None: return None
        Chem.Kekulize(m)
        return Chem.MolToSmiles(m, kekuleSmiles=True)
    except Exception:
        return None

def retrieve_taxonomy(path, n_workers=None):
    """Retrieve taxonomic class information for molecules in parallel."""
    # Set optimal worker count
    n_workers = n_workers or max(1, os.cpu_count() - 1)
    
    # Read input data
    df = pd.read_csv(path)
    smiles_lst = list(df.smiles)
    
    # Process SMILES in parallel
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as executor:
        processed_smiles = list(tqdm(
            executor.map(kekulize_smiles, smiles_lst),
            total=len(smiles_lst),
            desc="Processing SMILES"
        ))
    
    # Filter out None values
    processed_smiles = [s for s in processed_smiles if s is not None]
    
    # Get taxonomy information
    smiles_table, _ = drugtax.retrieve_taxonomic_class(
        processed_smiles, 
        input_mode="smiles_list", 
        output_name="testing", 
        write_values=True
    )
    
    # Get feature keys
    if len(smiles_table) > 0:
        # Extract features in parallel
        def get_features(smile):
            try:
                drug_tax = drugtax.DrugTax(smile)
                return drug_tax.features.values()
            except:
                return None
        
        smiles_to_process = list(smiles_table['SMILE'])
        f_keys = drugtax.DrugTax(smiles_to_process[0]).features.keys()
        
        # Process features in parallel
        with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as executor:
            feature_results = list(tqdm(
                executor.map(get_features, smiles_to_process),
                total=len(smiles_to_process),
                desc="Extracting features"
            ))
        
        # Create results dataframe
        valid_indices = [i for i, res in enumerate(feature_results) if res is not None]
        valid_smiles = [smiles_to_process[i] for i in valid_indices]
        valid_features = [feature_results[i] for i in valid_indices]
        
        # Create final dataframe
        result_df = pd.DataFrame({'SMILE': valid_smiles})
        df_final = pd.DataFrame([dict(zip(f_keys, feat)) for feat in valid_features])
        return pd.concat([result_df, df_final], axis=1)
    
    return pd.DataFrame()

if __name__ == "__main__":
    file_path = sys.argv[1]
    output_path = sys.argv[2]
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else None
    
    dout = retrieve_taxonomy(file_path, n_workers=workers)
    dout.to_csv(output_path, index=False)
