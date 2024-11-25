# Inactivity Monitor Script

## Overview

This Python script monitors user inactivity and puts your macOS computer to sleep after a specified timeout (default: 5 minutes). It runs as a background service and starts automatically when you log in.

## Features

- Detects user inactivity (basic support for macOS).
- Automatically puts the system to sleep after the specified timeout.
- Runs in the background with auto-start enabled.

## Requirements

- Python 3.x installed on your macOS system.
- Permissions to use `pmset` for sleep commands.

## Setup Instructions

1. **Clone the Repository**

   Download or clone the script file (`monitor_inactivity.py`) to your desired directory.

2. **Modify the Script**

   Ensure the script is configured to use the macOS `pmset sleepnow` command. If needed, update the timeout parameter in the `monitor_inactivity()` function (default: 300 seconds).

3. **Create a Launch Agent**

   Create a Launch Agent File:

   Open a terminal and create a new `.plist` file:

   ```bash
   nano ~/Library/LaunchAgents/com.inactivity.monitor.plist
   ```

   Add the Following Content:

   Replace `/path/to/monitor_inactivity.py` with the full path to your script.

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <plist version="1.0">
     <dict>
       <key>Label</key>
       <string>com.inactivity.monitor</string>
       <key>ProgramArguments</key>
       <array>
         <string>/usr/bin/python3</string>
         <string>/path/to/monitor_inactivity.py</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
       <key>KeepAlive</key>
       <true/>
     </dict>
   </plist>
   ```

   Save and Exit:

   Press `CTRL + O` to save, then `CTRL + X` to exit.

4. **Load and Start the Launch Agent**

   Load the Agent:

   ```bash
   launchctl load ~/Library/LaunchAgents/com.inactivity.monitor.plist
   ```

   Verify the Agent is Running:

   ```bash
   launchctl list | grep com.inactivity.monitor
   ```

   Check Logs for Errors: If the script does not behave as expected, check the system logs:

   ```bash
   log show --predicate 'process == "python3"' --info
   ```

5. **Testing**

   Temporarily set a shorter timeout in the script (e.g., 10 seconds).
   Run the script and leave your computer idle for the specified time.
   Ensure the system goes to sleep.

## Stopping the Script

Unload the Launch Agent:

```bash
launchctl unload ~/Library/LaunchAgents/com.inactivity.monitor.plist
```

Delete the Launch Agent (Optional):

```bash
rm ~/Library/LaunchAgents/com.inactivity.monitor.plist
```

## Known Limitations

- **Idle Detection**: macOS lacks built-in Python libraries for idle time detection. To enhance functionality, consider using third-party libraries like `pynput` or external tools.
- **Permissions**: Ensure the script has the required permissions to execute `pmset`.

## Optional Enhancements

- **Logging**: Add logging to a file for debugging:

  ```python
  with open("/path/to/activity_log.txt", "a") as log:
      log.write(f"Inactivity detected at {time.ctime()}\n")
  ```

- **Custom Sleep Timeout**: Modify the script to allow setting the timeout from the command line.

