import datetime

import psutil

PROCESS = "python3.11"
INFO = ["Proceso: ", "ID: ", "Proceso padre: ", "Ruta del proceso: ",
        "Llamado como: ", "Llamado por el usuario: ", "Estado: ", "Creado el "]


def get_process(process):
    for proc in psutil.process_iter(['name']):
        print(proc.info['name'])
        if proc.info['name'] == process:
            return proc


if __name__ == '__main__':
    proc = get_process(PROCESS)

    if proc:
        year, month, day, hour, minute, second = datetime.datetime.fromtimestamp(
            proc.create_time()).strftime("%Y %m %d %H %M %S").split()
        print(INFO[0], proc.name())
        print(INFO[1], proc.pid)
        print(INFO[2], proc.ppid(), "-", proc.parent().name())
        print(INFO[3], proc.exe())
        print(INFO[4], proc.cmdline())
        print(INFO[5], proc.username())
        print(INFO[6], proc.status())
        print(INFO[7], f"{year}-{month}-{day} a las {hour}:{minute}:{second}")
    else:
        print(f'El proceso {PROCESS} no existe')
