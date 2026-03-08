import pandas as pd
from pathlib import Path
import numpy as np


def extract_scores(myJobName):
    myJobName = myJobName
    csv_file_path = f"./ADMET/results/{myJobName}/pred.csv"

    df = pd.read_csv(csv_file_path)


    row = df.iloc[0]

    # Pick the 5 “dashboard” axes (use percentiles so everything is already 0–100)
    axes = {
        "Blood-Brain Barrier Safe": "BBB_Martins_drugbank_approved_percentile",
        "hERG Safe": "hERG_drugbank_approved_percentile",
        "Bioavailable": "Bioavailability_Ma_drugbank_approved_percentile",
        "Soluble": "Solubility_AqSolDB_drugbank_approved_percentile",
    }

    # A simple “Non-Toxic” score as the average of several toxicity-related percentiles
    tox_percentile_cols = [
        "ClinTox_drugbank_approved_percentile",
        "AMES_drugbank_approved_percentile",
        "DILI_drugbank_approved_percentile",
        "Carcinogens_Lagunin_drugbank_approved_percentile",
        "Skin_Reaction_drugbank_approved_percentile",
    ]
    non_toxic = float(np.mean([row[c] for c in tox_percentile_cols if c in df.columns]))

    labels = list(axes.keys()) + ["Non-Toxic"]
    values = [float(row[col]) for col in axes.values()] + [non_toxic]

    print(labels)
    print(values)

    print('BBB_Martins:', df.loc[0,'BBB_Martins'])
    print('BBB_Martins_drugbank_approved_percentile:', df.loc[0,'BBB_Martins_drugbank_approved_percentile'])


    # print(df.columns)

# run through each sample and get the values
smi_folder = Path("ADMET/test_samples_smiles")

for smi_file in smi_folder.glob("*.smi"):
    myJobName = smi_file.stem   # 👉 "samples_1"

    with open(smi_file, "r") as f:
        for line in f:
            smiles = line.strip().split()[0]   # first column is SMILES
            
            print("File:", myJobName)
            print("SMILES:", smiles)

            extract_scores(myJobName)
            print("___________________________________________________________\n")