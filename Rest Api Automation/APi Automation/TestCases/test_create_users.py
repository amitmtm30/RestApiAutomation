import requests
import json
import jsonpath
import pytest

# API url
url = "https://reqres.in/api/users"


@pytest.fixture()
def startup():
    global file
    file = open("D:\\Rest Api Automation\\APi Automation\\createuser.json", 'r')


@pytest.mark.Smoke
def test_create_new_user_001(startup):
    # open json file
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
    # jason_response = json.loads(response.text)
    # print(jason_response)
    # id_value = jsonpath.jsonpath(jason_response, 'id')
    # print(id_value[0])


@pytest.mark.Sanity
def test_create_other_user_002(startup):
    # open json file
    # Read the file
    request = file.read()
    # change the file to json format
    request_json = json.loads(request)
    # print(request_json)
    # create the request and send it
    response = requests.post(url, request_json)
    # print(response)
    # print(response.status_code)
    # assert response.status_code == 201
    file.close()
    # parsing the response in json format
    jason_response = json.loads(response.text)
    print(jason_response)
    id_value = jsonpath.jsonpath(jason_response, 'id')
    print(id_value[0])
