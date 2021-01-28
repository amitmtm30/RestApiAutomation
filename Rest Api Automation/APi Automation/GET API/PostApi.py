import requests
import json
import jsonpath

# API url
url = "https://reqres.in/api/users"
# Now Open the jason file
file = open("D:\\Rest Api Automation\\APi Automation\\Request.json", 'r')
# Reading the json file
jason_input = file.read()
# Parse the data in to json format
requests_jason = json.loads(jason_input)
print(requests_jason)

# Now make the json request and send it
response_body = requests.post(url, requests_jason)
print(response_body.content)
assert response_body.status_code == 201
# Closing the file
file.close()
# Fetch header from response
print(response_body.headers)

# fetch Content type from Header
print(response_body.headers.get('Content-Type'))

# Fetch Content Length form Header
print(response_body.headers.get('Content-Length'))

# Parse the Response to json format
response_json = json.loads(response_body.text)
# PicK ID form the response
id_value = jsonpath.jsonpath(response_json, 'id')
print(id_value[0])
