#!/usr/bin/python3
"""
Using the provided REST API and the given ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com/"
    todo_res = requests.get(f"{baseUrl}users/{user_id}/todos")
    user_res = requests.get(f"{baseUrl}users/{user_id}")

    if todo_res.status_code == 200 and user_res.status_code == 200:
        todo, user = todo_res.json(), user_res.json()
        completed_tasks = [task for task in todo if task.get('completed')]
        tasks_len = sum(1 for task in todo if task['userId'] == user_id)

        print(f"Employee {user.get('name')} is done with tasks"
              f"({len(completed_tasks)}/{tasks_len}):")

        for task in completed_tasks:
            print(f"\t {task['title']}")
