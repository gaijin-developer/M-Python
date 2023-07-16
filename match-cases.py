todos = []

while True:
    user_action = input("Type,add, show or exit \n")
    
    match user_action:
        case 'add':
            todo =input('enter a  todo : \n')
            cap_todo = todo.capitalize()
            todos.append(cap_todo)
        case 'show':
            print (todos)
        case 'exit':
            break

print('enjoy your day')

