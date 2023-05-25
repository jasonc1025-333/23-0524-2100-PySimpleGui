###jwc o import PySimpleGUI as sg
###jwc n 'step_size' is 'str' error: import PySimpleGUIWeb as sg
import PySimpleGUI as sg

from random import randint

GRAPH_SIZE = (400,200)
GRAPH_STEP_SIZE = 5

sg.change_look_and_feel('LightGreen')

layout = [  [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='-GRAPH-', background_color='lightblue'),],
            [sg.Text('Milliseconds per sample:', size=(20,1)),
             sg.Slider((0,30), default_value=15, orientation='h', key='-DELAY-')],
            [sg.Text('Pixels per sample:', size=(20,1)),
            ###jwc o  sg.Slider((1,30), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
             sg.Slider((0,30), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
            [sg.Button('Exit')]]

window = sg.Window('Animated Line Graph Example', layout)

delay = x = lastx = lasty = 0
while True:                             # Event Loop
    event, values = window.read(timeout=delay)
    if event in (None, 'Exit'):
        break
    step_size, delay = values['-STEP-SIZE-'], values['-DELAY-']
    y = randint(0,GRAPH_SIZE[1])        # get random point for graph
    if x < GRAPH_SIZE[0]:               # if still drawing initial width of graph
        window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
        ###jwc 
        window['-GRAPH-'].DrawLine((lastx, lasty+10), (x, y+10), color='green', width=1)
    else:                               # finished drawing full graph width so move each time to make room
        ###jwc ? 'str' window['-GRAPH-'].Move(-step_size, 0)
        ###jwc y window['-GRAPH-'].Move(-1*int(step_size), 0)
        window['-GRAPH-'].Move(-step_size, 0)
        window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
        ###jwc 
        window['-GRAPH-'].DrawLine((lastx, lasty+10), (x, y+10), color='green', width=1)
        ###jwc ? 'str' x -= step_size
        ###jwc y x -= int(step_size)
        x -= step_size
    lastx, lasty = x, y
    ###jwc ? 'str' x += step_size
    ###jwc y x += int(step_size)
    x += step_size
window.close()