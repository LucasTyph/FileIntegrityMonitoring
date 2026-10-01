# File Integrity Monitoring

A simple app for monitoring and detecting possibly unauthorized file changes on a specified directory.

This tool creates a cryptographic baseline of a directory and, upon learning of an alteration in that directory, checks the current filesystem against that baseline, reporting any additions, removals, or modifications.

Intended as a learning project and practical exploration of endpoint security, filesystem monitoring, cryptographic hashing, and security event detection.

## Features

### Current:

- Create a cryptographic baseline of a directory
- Calculate SHA-256 hashes for monitored files
- Detect new, modified or deleted files
- Compare current filesystem against a baseline
- Continuous, real-time filesystem monitoring through watchdog
- Generate human-readable integrity reports

### Planned:

- File metadata monitoring
- Event severity levels
- Baseline management and versioning

## Usage

First, you must select a directory with the `--directory` flag. By doing so, the monitor saves its location and calculates a SHA-256 hash for each file inside the directory (recursively).

This information is stored as a **baseline**, which is then saved in order to be checked against in the future.

Then, the monitor initializes the **watchdog**. Running constantly, this portion of the program is rensponsible for monitoring any changes in the saved directory's files, be it a creation, deletion, modification, or a moved file, and calls a Handler function whenever it detects anything.

When that does happen, the monitor runs its checks against the baseline, verifying its integrity and checking for any creations, modifications, or deletions, and reporting its findings in a human-readable manner.

You can also run the program with the `--baseline`, or `-b`, option, which runs a new set of SHA-256 hashes for all files in the directory, setting that as the new baseline. The execution of the program happens as usual after that.