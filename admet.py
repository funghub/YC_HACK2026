import requests

api_key = "insert-api-key-here"
headers = {'x-api-key': api_key}
base_url = "https://app.tamarind.bio/api/"

params = {
  "jobName": "myJobName",
  "type": "admet",
  "settings": {
    "smilesStrings": []
  }
}
response = requests.post(base_url + "submit-job", headers=headers, json=params)
print(response.text)