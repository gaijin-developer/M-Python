todos = []

while True:
    user_action = input("Type,add, show or exit \n")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo =input('enter a  todo : \n')
            cap_todo = todo.capitalize()
            todos.append(cap_todo)
        case 'show':
            #show the elements of the todo list in this case
            for item in todos:
                print(item)
        case 'exit':
            break

print('enjoy your day')

