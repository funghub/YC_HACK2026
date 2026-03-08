import requests

import os

api_key = os.getenv("tamarind_api") # this is the variable I names in my ./bashrc file for my api key

api_key = api_key
headers = {'x-api-key': api_key}
base_url = "https://app.tamarind.bio/api/"

sdfFile = "/fileconverter/sdf_files/samples_1.sdf"
jobName = "myJobName"

# SDF to SMILES
def get_smiles(sdfFile,jobName):
    params = {
    "jobName": jobName,
    "type": "file-converter",
    "settings": {
        "inputFileType": "sdf",
        "sdfFile": sdfFile
    }
    }
    response = requests.post(base_url + "submit-job", headers=headers, json=params)
    print(response.text)

get_smiles(sdfFile,jobName)

