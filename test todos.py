import datetime
import json

#Read the file
with open('todos.json') as t:
    todos = json.load(t)
    
#Date for text
date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')     
#Date for title
rev_date = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M')


#Create a file
def create_file(id):
    with open(f'{id}_{rev_date}.txt', 'w') as opened_file:
        opened_file.write(f'# Сотрудник №{id}')
        opened_file.write(f'\n{date}')
        opened_file.write('\n\n## Завершённые задачи:')
                
        #Find completed tasks
        for todo in todos: 
            try:
                if todo['userId'] == id and todo['completed']:
                    if len(todo['title']) > 50:
                        opened_file.write('\n' + todo['title'][:50] + '...')
                    else:
                        opened_file.write('\n' + todo['title'])
            except KeyError:
                continue
                        
        opened_file.write('\n\n## Оставшиеся задачи:')
             
        #Find not completed tasks
        for todo in todos: 
            try:
                if todo['userId'] == id and not todo['completed']:
                    if len(todo['title']) > 50:
                        opened_file.write('\n' + todo['title'][:50] + '...')
                    else:
                        opened_file.write('\n' + todo['title'])
            except KeyError:
                continue    

#Determine the number of users
for todo in todos:
    try:
        max = todo['userId']
    except KeyError:
        continue


def main():
    try:
        for i in range(max):
            i += 1
            create_file(i)
    except Exception as error:
        print(error)
        
        
if __name__ == '__main__':
    main()