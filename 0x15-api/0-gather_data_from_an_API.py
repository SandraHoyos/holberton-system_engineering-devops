#!/usr/bin/python3

"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list
"""

import requests
import sys

if __name__ == '__main__':
    """Gets API endpoint, then identify a
    user to display completed task info"""
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(userId)).json()
    todo = requests.get(url + 'todos?userId={}'.format(userId)).json()
    completed = []

    for task in todo:
        if task.get("completed"):
            completed.append(task.get("title"))
    print("Employee {} is done with task({}/{}):"
          .format(user.get('name'), len(completed), len(todo)))
    for task in completed:
        print('\t', task)
