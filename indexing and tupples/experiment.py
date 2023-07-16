# todos = []

# while True:
#     user_action = input("Type add, show, edit or exit \n")
#     user_action = user_action.strip()
    
#     match user_action:
#         case 'add':
#             todo =input('enter a  todo : \n')
#             cap_todo = todo.capitalize()
#             todos.append(cap_todo)
#         case 'show' | 'display':
#             #show the elements of the todo list in this case
#             for item in todos:
#                 item = item.title()
#                 print(item)
#         case 'edit':
#             number = input("Please enter the number of todo to edit: \n")
#             number= int(number)
#             number = number - 1
#             new_value = input('please enter the new todo: \n')
#             todos[number] = new_value
#         case 'exit' | 'end':
#             break
#         case whatever:
#             print('unknown command')

# print('enjoy your day')


my_list = ['one','two','three']

fst= my_list[2]
fst= my_list.index('three')
my_list[1]='new item'

print(my_list)