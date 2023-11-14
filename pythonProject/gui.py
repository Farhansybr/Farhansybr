import function
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values= function.get_todo(),key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                            layout=[[label], [input_box, add_button],[list_box, edit_button]],
                            font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = function.get_todo()
            new_todo = values['todo']+ "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = function.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
