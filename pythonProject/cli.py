from function import get_todo, write_todos
import time

now = time.strftime("%b %d, &Y %H:%M:%S")
print("Sekarang", now)

while True:
    user_action = input("type add, show,completed, edit or exit :")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todo()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todo()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todo()

            new_todo = input("masukan todo baru: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("command error")
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[6:])

            todos = get_todo()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            todos.pop(number - 1)

            write_todos(todos)

            message = f"todo {todo_to_remove} sudah dihilangkan dari list"
            print(message)
        except IndexError:
            print("nomor error")
            continue


    elif user_action.startswith('exit'):
        break

    else:
        print("command tidak valid")

print("selesai")