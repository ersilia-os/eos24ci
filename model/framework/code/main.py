#imports
import pandas as pd
import drugtax
import os
import sys
from rdkit import Chem

root = os.path.dirname(os.path.abspath(__file__))

def retrieve_taxonomy(path):

	def kekulize_smiles(smile):
		m = Chem.MolFromSmiles(smile)
		canonical_smile = Chem.Kekulize(m)
		canonical_smile = Chem.MolToSmiles(m,kekuleSmiles=True)
		return canonical_smile

	df = pd.read_csv(path); 
	smiles_lst = list(df["smiles"] if "smiles" in df.columns else df["input"])
	smiles_lst = [kekulize_smiles(i) for i in smiles_lst]


	input_sep = ' '
	smiles_table, summary_table = drugtax.retrieve_taxonomic_class(smiles_lst, input_mode = "smiles_list", output_name = "testing", write_values = True)

	f_keys = drugtax.DrugTax(smiles_table['SMILE'][0]).features.keys()

	smiles_table['features'] = None

	smiles_table['features'] = smiles_table['SMILE'].apply(lambda x : drugtax.DrugTax(x).features.values())

	smiles_table['features'] = smiles_table['features'].apply(lambda x : dict(zip(f_keys, x)))

	df_final = pd.DataFrame(list(smiles_table['features']))

	smiles_table = smiles_table.drop(['Taxonomy', 'features'], axis = 1)

	smiles_table = pd.concat([smiles_table, df_final], axis = 1)

	return smiles_table 

replacements = {
    '.': 'dot',
    '=': 'eq',
    '#': 'hash',
    '@': 'at',
    '+': 'plus',
    '-': 'minus',
    '[': 'bracket',
    '(': 'paren',
    '\\': 'backslash',
    '/': 'slash'
}

def clean_column_name(col):
    col = col.lower()
    for symbol, replacement in replacements.items():
        col = col.replace(symbol, replacement)
    return col



if __name__ == "__main__":
    file_path = sys.argv[1]
    output_path = sys.argv[2]
    df = retrieve_taxonomy(file_path)
    df.columns = [clean_column_name(col) for col in df.columns]
    df.drop(columns=['smile'], inplace=True)
    df.to_csv(output_path, index=False)
    for file in ['testing.csv', 'testing_assess.csv']:
        if os.path.exists(os.path.join(root,"..", file)):
	        os.remove(file)
