import subprocess
from . import event_name

def execute_events(events: list):
    for event in events:
       subprocess.run(['sendevent', f'/dev/input/{event_name}'] + event)

def press(x:float, y:float):
    '''
    Press on the screen on coordenates x,y
    '''
    events = [
        ['3', '57', '211'],
        ['3', '53', f'{x}'],
        ['3', '54', f'{y}'],
        ['1', '330', '1'],
        ['0', '0', '0'],
        ['3', '57', '4294967295'],
        ['1', '330', '0'],
        ['0', '0', '0']
        ]
    execute_events(events)

def swipe(x1: float, y1: float, x2: float, y2: float):
    '''
    Swipe from coordenates (x1, y1) to (x2, y2)
    '''
    events = [
        ['3', '57', '160'],
        ['3', '48', '7'],
        ['3', '53', f'{x1}'],
        ['3', '54', f'{y1}'],
        ['1', '330', '1'],
        ['0', '0', '0'],
        ['3', '48', '6'],
        ['3', '53', f'{x2}'],
        ['3', '54', f'{y2}'],
        ['0', '0', '0'],
        ['3', '57', '4294967295'],
        ['1', '330', '0'],
        ['0', '0', '0']
        ]
    execute_events(events)