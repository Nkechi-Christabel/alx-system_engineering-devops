#!/usr/bin/python3
"""Script to export to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    todo_all_employees = {}

    for user in users:
        user_id = user.get("id")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        todo_list = [{"task": task.get("title"), "completed":
                     task.get("completed"), "username":
                     user.get("username")} for task in todos]

        todo_all_employees[user_id] = todo_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_all_employees, jsonfile, indent=4)
