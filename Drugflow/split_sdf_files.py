# split sdf file
from rdkit import Chem

suppl = Chem.SDMolSupplier("samples.sdf")

for i, mol in enumerate(suppl):
    writer = Chem.SDWriter(f"mol_{i+1}.sdf")
    writer.write(mol)
    writer.close()