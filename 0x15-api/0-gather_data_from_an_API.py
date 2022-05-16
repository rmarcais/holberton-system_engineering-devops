#!/usr/bin/python3
"""
Python script that, using the REST API, for a given enmployee ID,
returns information about his/her TODO list progress.
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    api_url = requests.get(url)
    username = api_url.json().get("name")

    api_url_todo = requests.get("{}/todos".format(url))
    completed = []
    total = len(api_url_todo.json())

    for value in api_url_todo.json():
        if value.get("completed") is True:
            completed.append(value.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(username, len(completed), total))
    for i in completed:
        print("\t {}".format(i))
