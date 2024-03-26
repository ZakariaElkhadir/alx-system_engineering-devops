#!/usr/bin/python3
"""script to export data in the CSV format"""
import csv
import requests
from sys import argv


def main(user_id):
    """api_request"""
    url_task = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        int(user_id))
    url_name = "https://jsonplaceholder.typicode.com/users/{}".format(
        int(user_id))
    response = requests.get(url_task)
    response_name = requests.get(url_name)
    data = response.json()
    data_name = response_name.json().get('name')
    task_done = ['\t {}\n'.format(dic.get('title')) for dic in data
                 if dic.get('completed') is True]
    if data_name and data:
        print("Employee {} is done with tasks({}/{}):".format(
            data_name, len(task_done), len(data)))
        print("".join(task_done), end='')
        csv_file = "{}.csv".format(user_id)
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for row in data:
                writer.writerow(
                    [row.get('userId'), data_name,  row.get(
                        'completed'), row.get('title')])


if __name__ == "__main__":
    """Entry point"""
    main()
