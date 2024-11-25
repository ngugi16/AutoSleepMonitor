import os
import time
import ctypes
import platform


# Get the idle time in seconds (Windows only)
def get_idle_time():
    if platform.system() == "Windows":
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

        lii = LASTINPUTINFO()
        lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000.0  # Convert to seconds
    else:
        # For non-Windows platforms, you might need to use external libraries or tools.
        raise NotImplementedError("Idle time detection is currently Windows-only.")

# Put the system to sleep
def put_system_to_sleep():
    system = platform.system()
    if system == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif system == "Linux":
        os.system("systemctl suspend")
    elif system == "Darwin":  # macOS
        os.system("pmset sleepnow")
    else:
        raise NotImplementedError(f"Sleep command is not implemented for {system}")

# Monitor inactivity and trigger sleep
def monitor_inactivity(timeout=300):  # 5 minutes = 300 seconds
    try:
        while True:
            if platform.system() == "Windows":
                idle_time = get_idle_time()
                print(f"Idle Time: {idle_time:.2f} seconds")
                if idle_time > timeout:
                    print("System inactive for 5 minutes. Going to sleep...")
                    put_system_to_sleep()
                    break
            else:
                print("Idle time detection is not supported on this platform. Only Windows is fully supported.")
                break
            time.sleep(10)  # Check every 10 seconds
    except NotImplementedError as e:
        print(e)


if __name__ == "__main__":
    timeout = int(os.environ.get("IDLE_TIMEOUT", 300))
    monitor_inactivity(timeout)

