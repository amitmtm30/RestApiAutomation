import openpyxl
import requests
import json
import jsonpath
from DataDriven import Library


def test_add_multiple_student():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    # open the student json file in read mode
    file = open("D:\\RestApiProject\\Project1\\addstudent.json")
    json_file = file.read()
    json_request = json.loads(json_file)

    obj = Library.Common("D:\\RestApiProject\\Project1\\MultipleData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    key_list = obj.fetch_key_name()

    for i in range(2, row+1):
        updated_json_request = obj.update_request_with_data(i, json_request, key_list)
        response = requests.post(api_url, updated_json_request)
        print(response)
