from src.config_baseline import create_baseline, get_baseline, save_config, load_config
from src.hash import hash_all
from src.monitor import compare
from src.report import print_report

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import threading
import argparse

def main():
    print("Starting File Integrity Manager.")
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--directory",
        help="Directory to operate on",
    )

    parser.add_argument(
        "-b", "--baseline",
        action="store_true",
        help="Create a new baseline for the current directory",
    )

    args = parser.parse_args()

    if args.directory:
        directory_path = Path(args.directory)

        if not directory_path.exists():
            parser.error(f"Directory {directory_path} does not exist.")
        if not directory_path.is_dir():
            parser.error(f"Path {directory_path} is not a directory.")

        try:
            directory = directory_path.resolve()
        except OSError as e:
            parser.error(f"Could not resolve directory: {e}")

        try:
            save_config (directory)
        except OSError as e:
            parser.error(f"Could not save directory configuration: {e}")

        print(f"New directory saved: {directory}")
        new_dir = True

    else:
        try:
            directory = load_config()
        except OSError as e:
            parser.error(f"Could not load directory configuration: {e}")

        if (directory == None):
            parser.error("Please add a directory to check via the --directory flag!")

        directory_path = Path(directory)

        if not directory_path.exists():
            parser.error(f"Saved directory {directory_path} does not exist.")
        if not directory_path.is_dir():
            parser.error(f"Saved directory {directory_path} is no longer a directory.")
        
        print(f"Loaded saved directory: {directory}")
        new_dir = False

    if (new_dir or args.baseline):
        print(f"Creating baseline for directory {directory}")
        start(directory)
    
    watchdog(directory)

def start(directory: str):
    data = hash_all(directory)
    create_baseline(data)


def check(directory: str):
    currentData = hash_all(directory)
    baselineData = get_baseline()

    diff = compare(baselineData, currentData)
    print_report(diff)

def watchdog(path: str):
    observer = Observer()
    observer.schedule(Handler(path), path, recursive=True)
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
    def __init__(self, directory: str):
        self.directory = directory
        self.timer = None
        self.lock = threading.Lock()

    def trigger_check(self):
            with self.lock:
                if self.timer is not None:
                    self.timer.cancel()
    
                self.timer = threading.Timer(
                    2.0,
                    check,
                    args=(self.directory,)
                )
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