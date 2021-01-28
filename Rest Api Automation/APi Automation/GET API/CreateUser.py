import requests
import json
import jsonpath

# API url
url = "https://reqres.in/api/users"

# open json file
file = open("D:\\Rest Api Automation\\APi Automation\\createuser.json", 'r')
# Read the file
request = file.read()
# change the file to json format
request_json = json.loads(request)
print(request_json)

# create the request and send it
response = requests.post(url, request_json)
print(response)
print(response.status_code)
assert response.status_code == 201
file.close()

# parsing the response in json format
jason_response = json.loads(response.text)
print(jason_response)
id_value = jsonpath.jsonpath(jason_response, 'id')
print(id_value[0])


