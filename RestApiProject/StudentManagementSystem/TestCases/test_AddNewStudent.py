import requests
import json
import jsonpath


# POST and GET Request
def test_add_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    # open the json file in read mode
    file = open("D:\\RestApiProject\\StudentManagementSystem\\requestjson.json", 'r')
    # Reading the file
    json_file = file.read()
    # parsing the file  in to json format
    json_request = json.loads(json_file)
    # creating POST request as we are creating a new request
    response = requests.post(api_url, json_request)
    print(response.text)
    file.close()


def test_get_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/89621"
    response = requests.get(api_url)
    # parse response in to json format
    # json_response = json.loads(response.text)
    json_response = response.json()
    id1 = jsonpath.jsonpath(json_response, 'data.id')
    print(id1[0])
    assert id1[0] == 89621


# PUT Request
def test_update_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/89621"
    # open the json file in read mode
    file = open("D:\\RestApiProject\\StudentManagementSystem\\putrequest.json", 'r')
    # Reading the file
    json_file = file.read()
    # parsing the file  in to json format
    json_request = json.loads(json_file)
    # creating POST request as we are creating a new request
    response = requests.put(api_url, json_request)
    print(response.text)
    # parse the response
    response_jason = json.loads(response.text)
    out_status = jsonpath.jsonpath(response_jason, 'status')
    out_msg = jsonpath.jsonpath(response_jason, 'msg')
    print(out_msg[0])
    file.close()


def test_get_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/89621"
    response = requests.get(api_url)
    # parse response in to json format
    json_response = json.loads(response.text)
    json_response = response.json()
    print(json_response)


def test_delete_student():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/89621"
    response = requests.delete(api_url)


def test_get_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/89621"
    response = requests.get(api_url)
    # parse response in to json format
    json_response = json.loads(response.text)
    json_response = response.json()
    print(json_response)


