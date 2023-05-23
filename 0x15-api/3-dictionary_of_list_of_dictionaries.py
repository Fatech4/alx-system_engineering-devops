#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress.
"""
import csv
import json
import sys
import urllib.request


def fetch_employee_todo_progress():
    """ Function that implement the logic """
    try:
        # Fetch employee data
        employee_url = "https://jsonplaceholder.typicode.com/users"
        employee_response = urllib.request.urlopen(employee_url)
        employee_data = json.loads(employee_response.read())

        # Fetch TODO data for the employee
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos_response = urllib.request.urlopen(todos_url)
        todos_data = json.loads(todos_response.read())

        # Create a dictionary to store TODO progress by employee ID
        todo_progress = {}

        # Process employee data
        for employee in employee_data:
            employee_id = employee["id"]
            employee_name = employee["username"]

            # Filter TODO data for the current employee
            employee_todos = [
                    task for task in todos_data if task["userId"]
                    == employee_id]

            # Extract task information and store in the dictionary
            tasks = []
            for task in employee_todos:
                task_info = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                }
                tasks.append(task_info)

            todo_progress[employee_id] = tasks

        # Export to JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode="w") as json_file:
            json.dump(todo_progress, json_file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    fetch_employee_todo_progress()
