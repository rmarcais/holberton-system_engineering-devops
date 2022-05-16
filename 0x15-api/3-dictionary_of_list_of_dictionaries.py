#!/usr/bin/python3
"""
Python script that exports data using the CSV format.
Records all tasks from all employees
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/users/"
    api_url = requests.get(url)
    dictionary = {}

    for values in api_url.json():
        username = values.get("username")
        uid = values.get("id")
        api_url_todo = requests.get("{}{}/todos".format(url, uid))
        todo_list = []
        for value in api_url_todo.json():
            dico = {"username": username,
                    "task": value.get("title"),
                    "completed": value.get("completed")}
            todo_list.append(dico)
        dictionary[uid] = todo_list
    json_object = json.dumps(dictionary)
    with open(filename, "a") as f:
        f.write(json_object)
