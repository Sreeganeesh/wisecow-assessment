import psutil

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    if cpu > 80 or memory > 80 or disk > 80:
        print("⚠️ ALERT: System resource usage is high!")
    else:
        print("✅ System health is good.")

if __name__ == "__main__":
    check_system_health()
