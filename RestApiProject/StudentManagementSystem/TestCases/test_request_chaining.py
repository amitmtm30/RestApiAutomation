import requests
import json
import jsonpath


def test_add_new_student():
    global id1
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    # open the json file in read mode
    file = open("D:\RestApiProject\StudentManagementSystem\studentdetails.json", 'r')
    # Reading the file
    json_file = file.read()
    # parsing the file  in to json format
    json_request = json.loads(json_file)
    # creating POST request as we are creating a new request
    response = requests.post(api_url, json_request)
    print(response.text)
    response_json = json.loads(response.text)
    id1 = jsonpath.jsonpath(response_json, 'id')
    print(id1[0])
    file.close()


def test_get_student_details():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/"+str(id1[0])
    response = requests.get(api_url)
    print(response.text)
