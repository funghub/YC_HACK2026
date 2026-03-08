from rdkit import Chem

def conver_file(input_file):
    input_sdf = input_file
    output_smi = f"ADMET/test_samples_smiles/{input_file.stem}.smi"

    supplier = Chem.SDMolSupplier(input_sdf)

    with open(output_smi, "w") as f:
        for i, mol in enumerate(supplier):
            if mol is not None:
                smiles = Chem.MolToSmiles(mol)
                name = mol.GetProp("_Name") if mol.HasProp("_Name") else f"mol_{i}"
                f.write(f"{smiles}\t{name}\n")


from pathlib import Path

folder = Path("ADMET/test_samples_smiles")
folder.mkdir(exist_ok=True)

folder = Path("ADMET/test_samples_sdf")

for file in folder.glob("*.sdf"):
    input_file = file
    conver_file(input_file)
