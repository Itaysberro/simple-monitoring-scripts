import os
import time
import datetime

def check_internet():
    # Send ping to google.
    response = os.system("ping -n 1 8.8.8.8 > nul")
    if response == 0:
        return True
    else:
        return False

def write_log(message):
    # Add timeStamp.
    with open("internet_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

def main():
    while True:
        if check_internet():
            print("Succses")
        else:
            print("No internet")
            write_log("No internet connection.")
        
        time.sleep(5)  # Recheck every 5 sec.

if __name__ == "__main__":
    main()
