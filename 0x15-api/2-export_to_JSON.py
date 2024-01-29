#!/usr/bin/python3
"""
Using the provided REST API and the given ID, returns information about
his/her TODO list progress and exports it in JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/"
    todos_res = requests.get(f"{baseUrl}users/{user_id}/todos")
    user_res = requests.get(f"{baseUrl}users/{user_id}")

    if todos_res.status_code == 200 and user_res.status_code == 200:
        todos, user = todos_res.json(), user_res.json()

    json_data = {str(user_id): [{"task": task['title'], "completed":
                 task['completed'], "username": user.get('username')}
                 for task in todos]}

    with open(f"{user_id}.json", 'w') as jsonfile:
        json.dump(json_data, jsonfile)
