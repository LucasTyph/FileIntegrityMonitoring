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
