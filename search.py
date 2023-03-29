import requests
from urllib3.filepost import encode_multipart_formdata, choose_boundary
from azure.identity import DefaultAzureCredential
import requests_toolbelt as tb
from io import BytesIO
import pydicom
import json

credential = DefaultAzureCredential()
#print(credential.credentials) # this can be used to find the index of the AzureCliCredential
token = credential.credentials[4].get_token('https://dicom.healthcareapis.azure.com')
bearer_token = f'Bearer {token.token}'

dicom_service_name = "https://azurehealththb-thbdicomservice.dicom.azurehealthcareapis.com"

base_url = f"{dicom_service_name}/v1"
url = f'{base_url}/instances'
headers = {'Accept':'application/dicom+json','Authorization':bearer_token}
params = {'PatientName':'M', 'fuzzymatching': True}
client = requests.session()
response = client.get(url, headers=headers, params=params) #, verify=False)
print(response)

# Read Response
response_dict = json.loads(response.text)
print(response_dict)