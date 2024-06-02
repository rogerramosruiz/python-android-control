import subprocess
event_file = 'event.txt'

def get_event_name(getevent_output:str):
    lines = getevent_output.splitlines()
    current_event = ''
    for line in lines:
        if 'add device' in line:
            current_event = line.split(':')[-1].split('/')[-1]
        if 'INPUT_PROP_DIRECT' in line:
            return current_event
    return None

def get_event():
    getevent_output = subprocess.check_output(['getevent', '-il']).decode("utf-8")
    event_name = get_event_name(getevent_output)
    if event_name:
        with open(event_file, 'w') as f:
            f.write(event_name)
        return event_name
    else:
        raise Exception("Couldn't get event for touchscreen try running as a super user")

def load_event():
    with open(event_file, 'r') as f:
        return f.read()
    
if __name__ == '__main__':
    # get_event()
    print(load_event())