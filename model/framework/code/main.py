#imports
import pandas as pd
import drugtax
import sys
from rdkit import Chem

def retrieve_taxonomy(path):

	def kekulize_smiles(smile):
		m = Chem.MolFromSmiles(smile)
		canonical_smile = Chem.Kekulize(m)
		canonical_smile = Chem.MolToSmiles(m,kekuleSmiles=True)
		return canonical_smile

	df = pd.read_csv(path)
	smiles_lst = list(df.smiles)
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


if __name__ == "__main__":
    file_path = sys.argv[1]
    output_path = sys.argv[2]

    dout = retrieve_taxonomy(file_path)

    dout.to_csv(output_path)
