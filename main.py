from calculator import get_clicks
from colorize import get_clicks_color
from visualisator import visualise_clicks, visualise_interval
from asker import ask
from generations import generate_random_graph
import PySimpleGUI as sg


def print_reload(win_local,nums_local):
    clicks = get_clicks(list(map(int, nums_local.split())))
    colors = get_clicks_color(clicks)
    string_colors = "\n".join([f'{x[0]}->{x[1]}' for x in colors.items()])
    win_local['click_output'].update(f'Клики: {clicks}\n\nЦвета: \n{string_colors}')
    return clicks, colors


layout = [
    [sg.Text("Ввод интервального графа номерами начал и конца", tooltip="Например: '1 2 3 2 1 4 5 6 3 6 4 5'")],
    [sg.Input(size=(30, 0), key='main_input', default_text='1 2 3 2 1 4 5 6 3 6 4 5')],
    [sg.Button("Обновить", key='reload'), sg.Button("Вывод", key='print'), sg.Button("Сгенерировать", key='generate'),sg.Button("Интервалы",key='interval')],
    [sg.Text(key='click_output', size=(30, 20))]
]

win = sg.Window("Интервальный граф", layout=layout)

while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
        print("Спасибо за использование!")
        break

    if event == 'reload':
        print_reload(win,values['main_input'])

    if event == 'print':
        win.hide()
        visualise_clicks(*print_reload(win,values['main_input']))
        win.un_hide()

    if event == 'generate':
        nums = int(ask("максимально число:"))

        new_input = generate_random_graph(nums)
        win['main_input'].update(new_input)
        visualise_clicks(*print_reload(win,new_input))
        visualise_interval(list(map(int, new_input.split())))

    if event == 'interval':
        visualise_interval(list(map(int, values["main_input"].split())))
