import os, zipfile

api_key = os.getenv("tamarind_api")

import requests

api_key = api_key
headers = {'x-api-key': api_key}
base_url = "https://app.tamarind.bio/api/"

# VIEW THE JOB
params = {
}
response = requests.get(base_url + "jobs", headers=headers, params=params)
print(response.json())


# GET RESULTS
jobName = "myJobName" # add job name here

zip_path = os.path.join("./ADMET","results", f"{jobName}", f"{jobName}.zip") # file path for jobname
# savePath = f"./{jobName}.zip"
save_folder = os.path.join("./ADMET","results", f"{jobName}") # this creates the dir with job name for the file to save to
# save_folder = f"./ADMET/results/{jobName}"
os.makedirs(save_folder, exist_ok=True)

params = {
    "jobName": jobName
}


response = requests.post(base_url + "result", headers=headers, json=params)
print(response.text)
if response.status_code == 200:
    results = requests.get(response.text.replace('"', ''))
    if results.status_code == 200:
        with open(zip_path, 'wb') as file:
            file.write(results.content)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(save_folder)

print("Unzipped contents to:", save_folder)

            