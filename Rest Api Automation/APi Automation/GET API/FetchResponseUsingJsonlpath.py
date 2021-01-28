import requests
import json
import jsonpath

# API Url
url = "https://reqres.in/api/users?page=2"
# Sending the Request
response = requests.get(url)
# Parse Response to json format
json_response = json.loads(response.text)
print(json_response)
# Fetch value using json path
# Fetching the page count
page_value = jsonpath.jsonpath(json_response, 'page')
print(page_value[0])
# Fetching the total pages
pages = jsonpath.jsonpath(json_response, 'total')
print(pages[0])
