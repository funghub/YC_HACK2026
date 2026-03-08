import os

api_key = os.getenv("tamarind_api") # this is the variable I names in my ./bashrc file for my api key

import requests

api_key = api_key
headers = {'x-api-key': api_key}
base_url = "https://app.tamarind.bio/api/"


def get_predictions(myJobName, smiles):
  params = {
    "jobName": myJobName,
    "type": "admet",
    "settings": {
      "smilesStrings": [smiles]
    }
  }
  response = requests.post(base_url + "submit-job", headers=headers, json=params)
  print(response.text)


from pathlib import Path

smi_folder = Path("ADMET/test_samples_smiles")

for smi_file in smi_folder.glob("*.smi"):
    filename_stem = smi_file.stem   # 👉 "samples_1"

    with open(smi_file, "r") as f:
        for line in f:
            smiles = line.strip().split()[0]   # first column is SMILES
            
            print("File:", filename_stem)
            print("SMILES:", smiles)

            get_predictions(filename_stem, smiles)




