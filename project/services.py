import win32service
import win32serviceutil
from datetime import datetime, timedelta

def report_long_running_services(max_runtime_hours=24):
    sc_manager = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS)

    services = win32service.EnumServicesStatus(sc_manager, win32service.SERVICE_WIN32, win32service.SERVICE_STATE_ALL)

    for service in services:
        name, display_name, service_status = service[:3]
        if service_status[1] == win32service.SERVICE_RUNNING:
            # Service is running
            start_time = win32serviceutil.GetServiceStartDate(name)
            runtime = datetime.now() - start_time
            if runtime > timedelta(hours=max_runtime_hours):
                print(f"Long-running service: {display_name} (Running time: {runtime})")
        else:
            print(f"{display_name} is not running currently.")

    win32service.CloseServiceHandle(sc_manager)

report_long_running_services(24)
