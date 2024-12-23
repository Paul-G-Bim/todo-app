import r_w_todos
import FreeSimpleGUI as sg
# import time

sg.theme("Black")

# clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(size=10, image_filename="add.png", tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=r_w_todos.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[# [clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 10))

while True:
    event, values = window.read(timeout=10)
    # window['clock'].update(value=time.strftime("%b %m, %Y %I:%M:%S"))
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case 'Add':
            todos = r_w_todos.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            r_w_todos.write_todos(todos)

            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = r_w_todos.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                r_w_todos.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 10))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]

                todos = r_w_todos.get_todos()
                todos.remove(todo_to_complete)
                r_w_todos.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 10))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
