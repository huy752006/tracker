import os
import sqlite3
import shutil
from datetime import datetime, timedelta

def get_chrome_history():
    history_path = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\History"
    temp_copy = "temp_history.db"
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "browser_log.txt")

    try:
        shutil.copy2(history_path, temp_copy)
        conn = sqlite3.connect(temp_copy)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 20")

        with open(log_file, "w", encoding="utf-8") as f:
            for url, title, visit_time in cursor.fetchall():
                visit_time = datetime(1601, 1, 1) + timedelta(microseconds=visit_time)
                f.write(f"[{visit_time}] {title} - {url}\n")

        conn.close()
        os.remove(temp_copy)
    except Exception as e:
        print("Lỗi khi lấy lịch sử trình duyệt:", e)
