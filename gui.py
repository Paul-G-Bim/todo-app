import r_w_todos
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 10))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = r_w_todos.get_todos()
            todo = value['todo'] + '\n'
            todos.append(todo)
            r_w_todos.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
