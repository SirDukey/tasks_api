#!venv/bin/python
import requests, json

def get_data():
    done = input('DONE (y/n): ')
    if done == 'y':
        done = True
    elif done == 'n':
        done = False
    data = {
        'done': done, 
            }
    return data


if __name__ == '__main__':
    task_id = input('TASK ID: ')
    data = get_data()
    url = 'http://localhost:5000/todo/api/v1.0/tasks/' + task_id
    headers = {'content-type': 'application/json'}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    print('STATUS CODE:', r.status_code)
    print(r.json())