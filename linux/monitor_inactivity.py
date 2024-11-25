import os
import time
import platform


# Get the idle time in seconds (Linux only)
def get_idle_time():
    if platform.system() == "Linux":
        with open('/proc/uptime', 'r') as f:
            uptime, _ = map(float, f.readline().split())
        with open('/proc/stat', 'r') as f:
            for line in f:
                if line.startswith('btime'):
                    boot_time = float(line.split()[1])
                    break
        idle_time = uptime - (time.time() - boot_time)
        return idle_time
    else:
        raise NotImplementedError("Idle time detection is currently Linux-only.")


# Put the system to sleep
def put_system_to_sleep():
    system = platform.system()
    if system == "Linux":
        os.system("systemctl suspend")
    else:
        raise NotImplementedError(f"Sleep command is not implemented for {system}")


# Monitor inactivity and trigger sleep
def monitor_inactivity(timeout=300):  # 5 minutes = 300 seconds
    try:
        while True:
            if platform.system() == "Linux":
                idle_time = get_idle_time()
                print(f"Idle Time: {idle_time:.2f} seconds")
                if idle_time > timeout:
                    print("System inactive for 5 minutes. Going to sleep...")
                    put_system_to_sleep()
                    break
            else:
                print("Idle time detection is not supported on this platform. Only Linux is fully supported.")
                break
            time.sleep(10)  # Check every 10 seconds
    except NotImplementedError as e:
        print(e)


if __name__ == "__main__":
    timeout = int(os.environ.get("IDLE_TIMEOUT", 300))
    monitor_inactivity(timeout)

