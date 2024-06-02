import subprocess
from . import event_name

def press(x:float, y:float):
    """
    Press on the screen on coordenates x,y
    """
    events = [["sendevent", f"/dev/input/{event_name}", "3", "57", "211"],
            ["sendevent", f"/dev/input/{event_name}", "3", "53", f"{x}"],
            ["sendevent", f"/dev/input/{event_name}", "3", "54", f"{y}"],
            ["sendevent", f"/dev/input/{event_name}", "1", "330", "1"],
            ["sendevent", f"/dev/input/{event_name}", "0", "0", "0"],
            ["sendevent", f"/dev/input/{event_name}", "3", "57", "4294967295"],
            ["sendevent", f"/dev/input/{event_name}", "1", "330", "0"],
            ["sendevent", f"/dev/input/{event_name}", "0", "0", "0"]
    ]

    for event in events:
       subprocess.run(event)