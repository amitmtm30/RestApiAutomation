import requests
import json
import jsonpath


def test_add_new_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    # open the json file in read mode
    file = open("D:\\RestApiProject\\StudentManagementSystem\\requestjson.json", 'r')
    # Reading the file
    json_file = file.read()
    # parsing the file  in to json format
    json_request = json.loads(json_file)
    # creating POST request as we are creating a new request
    response = requests.post(api_url, json_request)
    # parse the response in to json format
    json_response = json.loads(response.text)
    student_id = jsonpath.jsonpath(json_response, 'id')
    print(" ")
    print("The Id of the newly student is : ", student_id[0])
    file.close()

    # adding technical details to the student
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    # open the json file in read mode
    file = open("D:\\RestApiProject\\StudentManagementSystem\\technicalDetails.json", 'r')
    # Reading the file
    json_file = file.read()
    # parsing the file  in to json format
    json_request = json.loads(json_file)
    # creating POST request as we are creating a new request
    response = requests.post(tech_api_url, json_request)
    jason_response = json.loads(response.text)
    print(jason_response)
    print("Technical Details Added Successfully")
    file.close()

    # Adding address to the student
    add_api_url = "http://thetestingworldapi.com/api/addresses"
    # open the json file in read mode
    file = open("D:\\RestApiProject\\StudentManagementSystem\\address.json", 'r')
    # Reading the file
    json_file = file.read()
    # parsing the file  in to json format
    json_request = json.loads(json_file)
    # creating POST request as we are creating a new request
    response = requests.post(add_api_url, json_request)
    file.close()

    # final details of the student
    api_url = "http://thetestingworldapi.com/api/FinalStudentDetails/89689"
    response = requests.get(api_url)
    print(response.text)
