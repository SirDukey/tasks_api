#!venv/bin/python
import requests, json

task_id = input('TASK ID: ')
url = 'http://localhost:5000/todo/api/v1.0/tasks/' + task_id

if __name__ == '__main__':
    r = requests.get(url)
    print('STATUS CODE:', r.status_code)
    res = json.loads(r.text)
    print(json.dumps(res, indent=2))