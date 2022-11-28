import humanize
import psutil

TEMPLATE = "{:48} {:>12} {:>12} {:>12} {:>12} {:>12}"
HEADER = ['Filesystem', 'Size', 'Used', 'Avail', 'Use %', 'Mounted on']

if __name__ == '__main__':
    print(TEMPLATE.format(*HEADER))
    for part in psutil.disk_partitions():
        disk = psutil.disk_usage(part.mountpoint)
        print(TEMPLATE.format(part.device, humanize.naturalsize(disk.total),
                              humanize.naturalsize(disk.used),
                              humanize.naturalsize(disk.free),
                              disk.percent, part.mountpoint))
