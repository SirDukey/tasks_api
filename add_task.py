#!venv/bin/python
import requests, json

def get_data():
    title = input('TITLE: ')
    description = input('DESCRIPTION: ')
    data = {
        'title': title, 
        'description': description
            }
    return data


if __name__ == '__main__':
    data = get_data()
    url = 'http://localhost:5000/todo/api/v1.0/tasks'
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print('STATUS CODE:', r.status_code)
    print(r.json())