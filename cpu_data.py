import psutil
import time
import multiprocessing

def get_cpu_usage_data(limit=5):
    usage = {}
    cpu_count = multiprocessing.cpu_count()

    # Warm-up call to initialize cpu_percent calculation
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Allow time for accurate CPU measurement
    time.sleep(0.1)

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            cpu = proc.info['cpu_percent'] / cpu_count  # Normalize by core count
            if cpu > 0:
                name = f"{proc.info['name']} (PID: {proc.info['pid']})"
                # Optionally exclude System Idle Process (PID 0)
                if "System Idle Process" not in name:
                    usage[name] = round(cpu, 1)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort and limit results
    sorted_usage = dict(sorted(usage.items(), key=lambda item: item[1], reverse=True)[:limit])
    return sorted_usage
