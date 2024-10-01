import tkinter as tk
from keylogger import start_keylogger, stop_keylogger

# GUI for controlling the keylogger
def create_gui():
    root = tk.Tk()
    root.title("Keylogger Control")

    # Button to start keylogger
    start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger, width=25)
    start_button.pack(pady=10)

    # Button to stop keylogger
    stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger, width=25)
    stop_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
