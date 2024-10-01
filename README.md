# Keylogger
This project is a simple keylogger written in Python using the `pynput` library. It captures and logs keystrokes, handling special keys and managing log files in a structured way by date. The project is intended for educational purposes and is designed to demonstrate the use of Python in monitoring keyboard events.

## Features

- **Keylogging**: Tracks all keyboard inputs, including special keys such as space, enter, backspace, and more.
- **Dynamic Log File Management**: Automatically creates log files, organized by date in folders, to manage logs efficiently.
- **Caps Lock and Shift Handling**: Correctly handles uppercase and lowercase characters depending on the state of caps lock and shift keys.
- **Backspace Handling**: Supports backspace by removing the last entered character from the log file.
- **Real-time Logging**: Updates log files in real-time as keystrokes are detected.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/keylogger.git
   cd keylogger

2. Install dependencies:
   ```bash
   pip install pynput

4. Run the keylogger:
   ```bash
   python keylogger.py
   
## Usage
The keylogger starts recording keystrokes as soon as the script is executed. It stores logs in a folder named logs, structured by year and date. Each log file is named based on the current date.
```plaintext
logs/
    ├── 2024/
    │   ├── log_2024-10-01.txt
    │   └── log_2024-10-02.txt
```
To stop the keylogger, simply terminate the script by closing the terminal or using a keyboard interrupt (Ctrl+C).

## Disclaimer
This project is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain proper consent before monitoring any system or individual's activity.

## Future Improvements
- Add encryption to log files for secure storage.
- Implement an email alert system to send logs periodically.
- Expand support for monitoring mouse events alongside keystrokes.
