import PySimpleGUI as sg


def ask(thing: str) -> str:
    layout = [
        [sg.Text(f'Ввод {thing}:')],
        [sg.Input(key='input')],
        [sg.Button('Ввод')]
    ]

    win = sg.Window(title='Спрашивалка', layout=layout)

    ans = win.read()[1]['input']
    win.close()
    return ans
