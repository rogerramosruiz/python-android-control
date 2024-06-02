import os
from .read_event import load_event, get_event

event_file = 'event.txt'
event_name = load_event() if os.path.exists(event_file) else get_event()