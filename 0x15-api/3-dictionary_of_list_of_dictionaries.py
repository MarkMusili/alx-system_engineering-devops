#!/usr/bin/python3
"""Dumps employee data into a json file"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    r = {user['id']: [{"task": item['title'],
                       "completed": item['completed'],
                       "username": user['username']} for item in todos
                      if item['userId'] == user['id']] for user in users}

    with open("todo_all_employees.json", "w") as f:
        json.dump(r, f)
