import psutil
import platform
from datetime import datetime

def get_system_health():
    report = []
    report.append(f"--- System Health Report ({datetime.now()}) ---")
    report.append(f"System: {platform.system()} {platform.release()}")
    report.append(f"CPU Usage: {psutil.cpu_percent()}%")
    report.append(f"Memory Usage: {psutil.virtual_memory().percent}%")
    report.append(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    report.append(f"Uptime (seconds): {int(psutil.boot_time())}")
    report.append("-" * 40)
    return "\n".join(report)

# Save report to a file
with open("health_log.txt", "a") as log_file:
    log_file.write(get_system_health() + "\n")
