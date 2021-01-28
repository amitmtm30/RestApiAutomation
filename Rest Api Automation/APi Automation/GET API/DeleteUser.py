import requests
import json
import jsonpath

# API url
url = "https://reqres.in/api/users/2"

# Delete API
response_delete = requests.delete(url)
print(response_delete)

assert response_delete.status_code == 204
