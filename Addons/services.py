import win32service
import win32serviceutil
import win32con
from datetime import datetime, timedelta

def report_long_running_services(max_runtime_hours=24):
    # Connect to the local Windows Service Manager
    scmanager = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS)

    # Enumerate services
    status = 1  # Service running
    services = win32service.EnumServicesStatus(scmanager, win32service.SERVICE_WIN32, win32service.SERVICE_STATE_ALL)
    
    for service in services:
        name, display_name, service_status = service[:3]
        if service_status[1] == win32service.SERVICE_RUNNING:
            # Service is running
            runtime = datetime.now() - win32serviceutil.GetServiceStartDate(name)
            if runtime > timedelta(hours=max_runtime_hours):
                print(f"Long-running service: {display_name} (Running time: {runtime})")
        else:
            print(f"{display_name} is not running currently.")

    win32service.CloseServiceHandle(scmanager)

# Example usage: report services running longer than 24 hours
report_long_running_services(24)
