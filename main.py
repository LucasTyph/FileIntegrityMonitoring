from src.baseline import create_baseline, get_baseline
from src.hash import hash_all
from src.monitor import compare
from src.report import print_report

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading

path_str = r"E:/tests"

def main():
    watchdog(path_str)

def start():
    data = hash_all(path_str)
    create_baseline(data)

def check():
    currentData = hash_all(path_str)
    baselineData = get_baseline()

    diff = compare(baselineData, currentData)
    print_report(diff)

def watchdog(path: str):
    observer = Observer()
    observer.schedule(Handler(), path, recursive=True)
    observer.start()
    print("Watchdog active!")

    try:
        while True:
            input()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Watchdog inactive.")

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.timer = None
        self.lock = threading.Lock()

    def trigger_check(self):
            with self.lock:
                if self.timer is not None:
                    self.timer.cancel()
    
                self.timer = threading.Timer(2.0, check)
                self.timer.start()

    def on_created(self, event):
        print("Created:", event.src_path)
        self.trigger_check()

    def on_deleted(self, event):
        print("Deleted:", event.src_path)
        self.trigger_check()

    def on_modified(self, event):
        print("Modified:", event.src_path)
        self.trigger_check()

    def on_moved(self, event):
        print("Moved:", event.src_path, "->", event.dest_path)
        self.trigger_check()

if __name__ == "__main__":
    main()