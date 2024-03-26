#!/usr/bin/python3
"""script to export data in the dictionary format"""
import json
import requests


def main():
    """api_request"""
    url_task = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url_task)
    data = response.json()
    data_dict = {}

    for dic in data:
        user_id = dic.get('userId')
        task_dict = {
            "task": dic.get('title'),
            "completed": dic.get('completed'), "username": dic.get('username')}
        if user_id not in data_dict:
            data_dict[user_id] = [task_dict]
        else:
            data_dict[user_id].append(task_dict)
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(data_dict, file)


if __name__ == "__main__":
    main()
