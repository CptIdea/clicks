import math

import PySimpleGUI as sg


def visualise_clicks(clicks, colors):
    layout = [
        [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(-105, -105), graph_top_right=(105, 105),
                  background_color='white', key='graph')]
    ]

    window = sg.Window('Graph of Sine Function', layout, grab_anywhere=True, finalize=True)
    graph = window['graph']

    y_count, x_count = 0, 0
    while y_count * x_count < len(colors):
        y_count += 1
        x_count += 1

    cords = {dot: get_cords(len(colors), dot) for dot in colors}

    for dot in cords:
        graph.draw_point(tuple([(n * 40) for n in cords[dot]]), size=5)
        graph.draw_text(f'{dot}({colors[dot]})', tuple([(n * 50) for n in cords[dot]]))

    for click in clicks:
        listed_click = list(click)
        for i in range(len(listed_click) - 1):
            for to_dot in listed_click[i + 1:]:
                graph.draw_line(point_from=tuple([(n * 40) for n in cords[listed_click[i]]]),
                                point_to=tuple([(n * 40) for n in cords[to_dot]]))

    window.read()
    window.close()


def get_cords(count, current_number):
    step = (2 * math.pi) / count
    return math.sin(step * current_number), math.cos(step * current_number)
