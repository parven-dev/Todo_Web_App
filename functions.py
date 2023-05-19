# from main import todos, user


def ReadFunction(filepath='todo_file_handling.txt'):
    with open(filepath, 'r') as f:
        todo_todo = f.readlines()

    return todo_todo


def WriteFunction(todos, filepath='todo_file_handling.txt'):
    with open(filepath, 'w') as f:
        f.writelines(todos)


# def ApeendFunction(filepath='todo_file_handling.txt'):
#     with open(filepath, 'a') as f:
#         f.writelines(user + '\n')
