#!venv/bin/python
import requests, json


if __name__ == '__main__':
    task_id = input('TASK ID: ')
    if task_id == '1':
        print('Sorry, task id 1 cannot be deleted')
        exit
    else:
        url = 'http://localhost:5000/todo/api/v1.0/tasks/' + task_id
        headers = {'content-type': 'application/json'}
        r = requests.delete(url, headers=headers)
        print('STATUS CODE:', r.status_code)
        print(r.json())