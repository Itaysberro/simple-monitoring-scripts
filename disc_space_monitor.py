import shutil
import time
from datetime import datetime

DISK_PATH = "C:\\"
MIN_FREE_SPACE_GB = 5  # Minimum free space in GB

def get_free_space_gb(path):
    # Get the free disk space in GB
    total, used, free = shutil.disk_usage(path)
    return free / (1024 * 1024 * 1024)

def write_log(message):
    with open("disk_space_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

def main():
    while True:
        free_space = get_free_space_gb(DISK_PATH)
        print(f"Free space: {free_space:.2f} GB")

        if free_space < MIN_FREE_SPACE_GB:
            warning_message = f"Low disk space! Only {free_space:.2f} GB left."
            print(warning_message)
            write_log(warning_message)
        else:
            print("Disk space is OK.")

        time.sleep(10)  # Wait 10 seconds before the next check

if __name__ == "__main__":
    main()
