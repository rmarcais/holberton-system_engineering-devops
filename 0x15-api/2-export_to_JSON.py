#!/usr/bin/python3
"""
Python script that exports data using the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    api_url = requests.get(url)
    username = api_url.json().get("username")
    uid = api_url.json().get("id")

    api_url_todo = requests.get("{}/todos".format(url))

    filename = "{}.json".format(argv[1])

    todo_list = []

    for value in api_url_todo.json():
        dico = {"task": value.get("title"),
                "completed": value.get("completed"),
                "username": username}
        todo_list.append(dico)
    dictionary = {uid: todo_list}
    json_object = json.dumps(dictionary)
    with open(filename, "w") as f:
        f.write(json_object)
