#!/usr/bin/python3
"""
Python script that exports data using the CSV format.
Records all tasks from all employees


import json
import requests

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
    with open(filename, "w") as f:
        json.dump(dictionary, f)"""
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
