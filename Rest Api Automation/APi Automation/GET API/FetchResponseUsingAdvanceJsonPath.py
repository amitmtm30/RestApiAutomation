import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
# parse this response to json format
json_response = json.loads(response.text)
print(json_response)

firstname = jsonpath.jsonpath(json_response,'data[1].first_name')
print((firstname[0]))

# fetch out all the first name from the response
for i in range(0, 7):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print((first_name[0]))

