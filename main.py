from src.baseline import create_baseline, get_baseline
from src.hash import hash_all
from src.monitor import compare

import json

def main():
    check()

def start():
    data = hash_all()
    create_baseline(data)

def check():
    currentData = hash_all()
    print (json.dumps(currentData))
    baselineData = get_baseline()
    print (json.dumps(baselineData))

    print (json.dumps(compare(baselineData, currentData)))

if __name__ == "__main__":
    main()