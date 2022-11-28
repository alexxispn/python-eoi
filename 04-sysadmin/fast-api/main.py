import datetime

import humanize
import psutil
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/memory")
def memory():
    return {
        "memory": {
            "total": humanize.naturalsize(psutil.virtual_memory().total),
            "used": humanize.naturalsize(psutil.virtual_memory().used),
            "free": humanize.naturalsize(psutil.virtual_memory().free),
            "shared": humanize.naturalsize(psutil.virtual_memory().shared),
            "buffers": humanize.naturalsize(psutil.virtual_memory().buffers),
            "cache": humanize.naturalsize(psutil.virtual_memory().cached),
        },
        "swap": {
            "total": humanize.naturalsize(psutil.swap_memory().total),
            "used": humanize.naturalsize(psutil.swap_memory().used),
            "free": humanize.naturalsize(psutil.swap_memory().free),
        },
    }


@app.get("/disk")
def disk():
    disks = {}
    for partition in psutil.disk_partitions():
        disks[partition.mountpoint] = {
            "Device": partition.device,
            "Total": humanize.naturalsize(
                psutil.disk_usage(partition.mountpoint).total),
            "Used": humanize.naturalsize(
                psutil.disk_usage(partition.mountpoint).used),
            "Free": humanize.naturalsize(
                psutil.disk_usage(partition.mountpoint).free),
            "Use": str(psutil.disk_usage(partition.mountpoint).percent) + "%",
            "Type": partition.fstype,
            "Mount": partition.mountpoint,
        }
    return disks


@app.get("/process")
def processes():
    processes = {}
    for proc in psutil.process_iter(
            ['name', 'pid', 'ppid', 'username', 'status', 'create_time']):
        processes[proc.info['name']] = {
            "name": proc.info['name'],
            "pid": proc.info['pid'],
            "ppid": proc.info['ppid'],
            "username": proc.info['username'],
            "status": proc.info['status'],
            "create_time": datetime.datetime.fromtimestamp(
                proc.info['create_time']).strftime("%Y-%m-%d %H:%M:%S"),
        }
    return processes


@app.get("/process/{process_name}")
def process(process_name: str):
    for proc in psutil.process_iter(
            ['name', 'pid', 'ppid', 'username', 'status', 'create_time']):
        if proc.info['name'] == process_name:
            return {
                process_name: {
                    "Proceso": proc.name(),
                    "ID": proc.pid,
                    "Proceso padre": f"{proc.ppid()} - {proc.parent().name()}",
                    "Ruta del proceso": proc.exe(),
                    "Llamado como": proc.cmdline(),
                    "Llamado por el usuario": proc.username(),
                    "Estado": proc.status(),
                    "Creado": f"Creado el {datetime.datetime.fromtimestamp(proc.create_time()).strftime('%Y-%m-%d a las %H:%M:%S')}",
                }
            }
    return {"message": f"Process {process_name} not found"}


if __name__ == "__main__":
    uvicorn.run(app)
