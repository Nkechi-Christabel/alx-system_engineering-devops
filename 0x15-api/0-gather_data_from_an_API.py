#!/usr/bin/python3
"""
Uses the provided REST API and the given ID, returns information about
his/her TODO list progress.
"""
from sys import argv
import requests

if __name__ == "__main__":
    user_id = int(argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com/"
    todo_res = requests.get(f'{baseUrl}todos')
    users_res = requests.get(f"{baseUrl}users")

    if todo_res.status_code == 200 and users_res.status_code == 200:
        todo, users = todo_res.json(), users_res.json()
        user = next((user for user in users if user['id'] == user_id), None)
        completed_tasks = [task for task in todo if task['userId'] == user_id
                           and task['completed']]
        tasks_len = sum(1 for task in todo if task['userId'] == user_id)

        print(f"Employee {user['name']} is done with tasks\
              ({len(completed_tasks)}/{tasks_len}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")
