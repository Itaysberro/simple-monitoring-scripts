import shutil
from datetime import datetime


DISK_PATH = "C:\\"

#Check disk space    
total, used, free = shutil.disk_usage(DISK_PATH)
free_gb = free / (1024 * 1024 * 1024)

# Generate report message
report_message = f"Free disk space on {DISK_PATH}: {free_gb:.2f} GB"


print(report_message)

#Write the report to a file
with open("disk_space_report.txt", "w") as report_file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_file.write(f"Disk Space Report - {timestamp}\n")
    report_file.write(report_message)
