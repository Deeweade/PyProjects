import os.path
import datetime

import requests
import json

response_users = requests.get("https://json.medrating.org/users")
response_todos = requests.get("https://json.medrating.org/todos")
if response_todos.status_code == response_users.status_code == 200:
    users = json.loads(response_users.text)
    todos = json.loads(response_todos.text)
else:
    print("Connection Error")

    
def file_change(a):
    date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    data = (f'{users[a]["name"]} <{users[a]["email"]}> {date}'
            f'\n{users[a]["company"]["name"]}\n\nЗавершённые задачи:\n')
    
    for j in range(len(todos)):
        if users[a]['id'] == todos[j]['userId']:
            if todos[j]['completed'] and todos[j]["title"] != '':
                if len(todos[j]["title"]) <= 50:
                    data = data + (f'{todos[j]["title"]}\n')
                else:
                    todos[j]["title"] = todos[j]["title"][:50]
                    data = data + (f'{todos[j]["title"]}...\n')
            else:
                continue

    data = data + (f'\nОставшиеся задачи:\n')

    for j in range(len(todos)):
        if users[a]['id'] == todos[j]['userId']:
            if not todos[j]['completed'] and todos[j]["title"] != '':
                if len(todos[j]["title"]) <= 50:
                    data = data + (f'{todos[j]["title"]}\n')
                else:
                    todos[j]["title"] = todos[j]["title"][:50]
                    data = data + (f'{todos[j]["title"]}...\n')
            else:
                continue
    
    file = open(f'{filename}.txt', 'x')
    file.write(data)
    file.close()
    
path = os.getcwd() + '/tasks'

for i in range(len(users)):
    filename = users[i]['username']
    check_dir = os.path.isdir(f'{path}')
    
    def check_file():    
        check_file = os.path.isfile(f'{filename}.txt')
        if not check_file:
            file_change(i)
        else:
            old_file = open(f'{filename}.txt', 'r')
            word = old_file.readline().rstrip().split(' ')
            old_date = word[len(word) - 2].split('.')
            old_date = 'T'.join([str(f'{old_date[2]}-{old_date[1]}'
                                f'-{old_date[0]}'), word[len(word) - 1]])
            old_file.close()
            os.rename(f'{filename}.txt', 
                      f'{filename}_{old_date}.txt')
            file_change(i)
    
    if not check_dir:
        os.mkdir(path)
        os.chdir(path)
        check_file()
        
    else:
        os.chdir(path)
        check_file()
        continue