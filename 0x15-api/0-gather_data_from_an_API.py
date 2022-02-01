#!/usr/bin/python3
""" returns information about his/her TODO list progress"""
import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]
    url = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(userId)).json()
    all = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(userId)).json()

    done = []
    for tasks in all:
        if tasks.get('completed'):
            done.append(tasks.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(url.get('name'), len(done), len(all)))
    print("\n".join("\t {}".format(tasks) for tasks in done))
