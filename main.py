
running = True
while running:
    task_menu = ["Add Task","View tasks", "Mark task as done","Exit"]
    for i,menu in enumerate(task_menu):
        print(f'{i + 1} : {menu}')

    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        print("add task selected!")
    elif user_choice == 2:
        print("View tasks selected!")
    elif user_choice == 3:
        print("Mark task as done!")
    else:
        running = False
        print("Exit")
print('goodbye')



# task_list = [
#     {'task_name': 'Do Grocery',
#      'task_status': False},
#     {'task_name': 'Do cleaning',
#      'task_status': False},
# ]
# user_input = input("Enter a task:")

# new_dict = {
#     'task_name': user_input,
#     'task_status': False
# }
# task_list.append(new_dict)

# program_running = True
# while program_running:

#     for i, task in enumerate(task_list):
#         print(f" {i + 1} : {task['task_name']} - {task['task_status']}")


#     user_done = int(input("Enter task number to mark as done:"))
#     index = user_done - 1
#     task_list[index]['task_status'] = True

#     for i, task in enumerate(task_list):
#         print(f" {i + 1} : {task['task_name']} - {task['task_status']}")
