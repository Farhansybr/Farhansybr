import function
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add",size=10)
list_box = sg.Listbox(values= function.get_todo(),key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Completed")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, &Y %H:%M:%S"))

    match event:
        case "Add":
            todos = function.get_todo()
            new_todo = values['todo']+ "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = function.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select the item first", font=("Helvetica", 10))

        case "Completed":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todo()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window["todos"].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select the item first", font=("Helvetica", 10))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
