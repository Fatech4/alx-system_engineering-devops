#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress.
"""
import urllib.request
import json
import sys


def fetch_employee_todo_progress(employee_id):
    """ Function that implement the logic """
    try:
        # Fetch employee data
        employee_url = "https://jsonplaceholder.typicode.com/users/{}"\
                .format(employee_id)
        employee_response = urllib.request.urlopen(employee_url)
        employee_data = json.loads(employee_response.read())

        # Fetch TODO data for the employee
        todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos"\
                    .format(employee_id)
        todos_response = urllib.request.urlopen(todos_url)
        todos_data = json.loads(todos_response.read())

        # Extract relevant information
        employee_name = employee_data["name"]
        total_tasks = len(todos_data)
        done_tasks = [task["title"] for task in todos_data if
                      task["completed"]]

        # Display output
        print(f"Employee {employee_name} is done with tasks\
              ({len(done_tasks)}/{total_tasks}): ")
        for task in done_tasks:
            print(f"\t{task}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
