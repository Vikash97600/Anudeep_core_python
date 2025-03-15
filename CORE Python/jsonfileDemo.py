#read the json data of a file jsonfileDemo.json and print the json data
import json
def read_json(file_path):
    with open(file_path,"r") as file:
        data=json.load(file)
    for item in data:
        if not isinstance(item.get('student_id'),int):
            print("student_id must be integer")
        if not isinstance(item.get('student_name'),str):
            print("student_name must be string")
        if not isinstance(item.get('student_address'),str):
            print("student_address must be string")

        # printing the json file data
        print(item)
read_json('jsondemo.json')