from r_w_todos import get_todos, write_todos
import time

now = time.strftime("%b %m, %Y %I:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("\nType add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        todos = [todo.strip('\n') for todo in todos]
        print('\n'.join(f"{index + 1}. {todo}" for index, todo in enumerate(todos)))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            todos = get_todos()
            todos[number] = input("Enter new todo: ") + '\n'
            write_todos(todos)

        except (IndexError, ValueError):
            print("Invalid entry.")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) - 1
            todos = get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            write_todos(todos)

            print(f"|**{todo_to_remove}**| was removed.")

        except (IndexError, ValueError):
            print("Invalid entry.")

    elif user_action == 'exit':
        break

    else:
        print("Unknown command")

print('Bye!')
