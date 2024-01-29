#!/usr/bin/python3
"""
Using the provided REST API and the given ID, returns information about
his/her TODO list progress and export it in csv.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/"
    todos_res = requests.get(f'{baseUrl}users/{user_id}/todos')
    user_res = requests.get(f"{baseUrl}users/{user_id}")

    todos, user = todos_res.json(), user_res.json()

    with open(f'{user_id}.csv', 'w') as file:
        for task in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, user['username'], task['completed'],
                               task['title']))
