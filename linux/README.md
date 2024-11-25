Run the Script in the Background
For Linux
Make the Script Executable:

```bash
chmod +x monitor_inactivity.py
```

Create a Systemd Service:

Open a terminal and create a new service file:

```bash
sudo nano /etc/systemd/system/inactivity_monitor.service
```

Add the following content to the file:

```ini
[Unit]
Description=Inactivity Monitor Script
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /path/to/monitor_inactivity.py
Restart=always
User=your-username

[Install]
WantedBy=multi-user.target
```

Replace `/path/to/monitor_inactivity.py` with the full path to your script, and `your-username` with your system username.

Enable and Start the Service:

```bash
sudo systemctl enable inactivity_monitor
sudo systemctl start inactivity_monitor
```

Check the Status: Verify the service is running:

```bash
sudo systemctl status inactivity_monitor
```

Stopping the Script
Linux
Stop the service:

```bash
sudo systemctl stop inactivity_monitor
```

macOS
Unload the agent:

```bash
launchctl unload ~/Library/LaunchAgents/com.inactivity.monitor.plist
```
