from calculator import get_clicks
from colorize import get_clicks_color
from visualisator import visualise_clicks
import PySimpleGUI as sg

layout = [
    [sg.Text("Ввод интервального графа номерами начал и конца", tooltip="Например: '1 2 3 2 1 4 5 6 3 6 4 5'")],
    [sg.Input(size=(30, 0), key='main_input',default_text='1 2 3 2 1 4 5 6 3 6 4 5')],
    [sg.Button("Обновить", key='reload'), sg.Button("Вывод", key='print')],
    [sg.Text(key='click_output', size=(30, 20))]
]

win = sg.Window("Интервальный граф", layout=layout)
clicks = []
colors = {}

while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
        print("Спасибо за использование!")
        break

    if event == 'reload':
        clicks = get_clicks(list(map(int, values["main_input"].split())))
        colors = get_clicks_color(clicks)
        string_colors = "\n".join([f'{x[0]}->{x[1]}' for x in colors.items()])
        win['click_output'].update(f'Клики: {clicks}\n\nЦвета: \n{string_colors}')

    if event == 'print':
        clicks = get_clicks(list(map(int, values["main_input"].split())))
        colors = get_clicks_color(clicks)
        win.hide()
        visualise_clicks(clicks,colors)
        win.un_hide()
