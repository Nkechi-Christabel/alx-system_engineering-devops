#!/usr/bin/python3
"""
Using the provided REST API and the given ID, returns information about
his/her TODO list progress and export it in csv.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com/"
    todos_res = requests.get(f"{baseUrl}todos")
    user_res = requests.get(f"{baseUrl}users/{user_id}")

    if todos_res.status_code == 200 and user_res.status_code == 200:
        todos, user = todos_res.json(), user_res.json()
        todos = [task for task in todos if task['userId'] == user_id]

    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user.get('username'),
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })
