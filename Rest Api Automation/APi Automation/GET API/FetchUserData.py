import requests

# API Url
url = "https://reqres.in/api/users?page=2"
# Send Get Request
response = requests.get(url)
print(response)

# Print the content of the request
print(response.content)

# verify the status of the response
assert response.status_code == 200
print("Success")
