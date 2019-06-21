#!venv/bin/python
import requests, json

url = 'http://localhost:5000/todo/api/v1.0/tasks/all'

if __name__ == '__main__':
    r = requests.get(url)
    res = json.loads(r.text)
    print('STATUS CODE:', r.status_code)
    print(json.dumps(res, indent=2))