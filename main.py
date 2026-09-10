from src.baseline import create_baseline, get_baseline
from src.hash import hash_all
from src.monitor import compare
from src.report import print_report

import json

def main():
    check()

def start():
    data = hash_all()
    create_baseline(data)

def check():
    currentData = hash_all()
    baselineData = get_baseline()

    diff = compare(baselineData, currentData)
    print_report(diff)


if __name__ == "__main__":
    main()