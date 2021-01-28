import requests

# API Url
url = "https://reqres.in/api/users?page=2"
# Sending the Request
response = requests.get(url)

# Fetch Response Headers
print(response.headers)
# Fetch Date from the response headers
print(response.headers.get("Date"))
# Fetch the content-type from response headers
print(response.headers.get("Content-Type"))
# Fetch the server from response headers
print(response.headers.get("server"))
print("#" * 10)
# Fetch Cookies from the response
print(response.cookies)
# Fetch Encoding
print(response.encoding)
# Fetch elapsed time
print(response.elapsed)
