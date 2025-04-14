import tkinter as tk
from browser_tracker import get_chrome_history
import os

def open_logs():
    os.startfile("logs")

def update_browser_history():
    get_chrome_history()
    label.config(text="Đã cập nhật lịch sử trình duyệt!")

def run_gui():
    global label
    window = tk.Tk()
    window.title("Parental Tracker")
    window.geometry("300x200")

    label = tk.Label(window, text="Chào bạn!", font=("Arial", 12))
    label.pack(pady=10)

    btn1 = tk.Button(window, text="Lấy lịch sử trình duyệt", command=update_browser_history)
    btn1.pack(pady=5)

    btn2 = tk.Button(window, text="Mở thư mục log", command=open_logs)
    btn2.pack(pady=5)

    window.mainloop()
