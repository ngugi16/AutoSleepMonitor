# Inactivity Monitor Script

## Overview

This Python script monitors system inactivity and puts the computer to sleep after a specified timeout (default is 5 minutes). It supports Windows, Linux, and macOS, running in the background with auto-start capabilities.

## Features

- Detects user inactivity (Windows-only for built-in idle time detection).
- Automatically puts the system to sleep after the specified timeout.
- Runs in the background with auto-start capabilities.

## Requirements

- Python 3.x installed on the system.
- Administrator/root privileges for setting up background tasks.

## Setup Instructions

1. **Clone the Repository**

   Clone or download the script file (`monitor_inactivity.py`) to your desired directory.

2. **Modify the Script**

   The script includes platform-specific commands for sleep and inactivity detection:
   - **Linux**: Uses `systemctl suspend`.
   - **macOS**: Uses `pmset sleepnow`.
   - **Windows**: Uses `rundll32.exe powrprof.dll,SetSuspendState 0,1,0`.

   If needed, update the timeout parameter in the `monitor_inactivity()` function.

3. **Run the Script**

   Execute the script with Python to start monitoring inactivity.

4. **Configure Auto-Start (Optional)**

   Set up the script to run automatically on system startup using platform-specific methods.

