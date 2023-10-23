#!/usr/bin/python3
"""script fetches info employee's ID using an api"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info
    user_url = '{}/users?id={}'.format(base_url, user_id)

    # get info
    response = requests.get(user_url)
    # pull data
    data = response.text
    # parse the data into JSON format
    data = json.loads(data)
    # extract user data
    name = data[0].get('name')

    # get user info about todo tasks
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    # get info from api
    response = requests.get(tasks_url)
    # pull data from api
    tasks = response.text
    # parse the data into JSON format
    tasks = json.loads(tasks)

    # initialize completed count as 0 and find total number of tasks
    completed = 0
    total_tasks = len(tasks)

    completed_tasks = []
    for task in tasks:
        if task.get('completed'):
            # print("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # print the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
