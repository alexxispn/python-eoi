import humanize
import psutil

TEMPLATE = "{:7} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}"
HEADER = ['', 'total', 'used', 'free', 'shared', 'buff', 'cache',
          'available']

if __name__ == '__main__':
    print(TEMPLATE.format(*HEADER))
    virt = psutil.virtual_memory()
    swap = psutil.swap_memory()
    print(TEMPLATE.format('Mem:', humanize.naturalsize(virt.total),
                          humanize.naturalsize(virt.used),
                          humanize.naturalsize(virt.free),
                          humanize.naturalsize(virt.shared),
                          humanize.naturalsize(virt.buffers),
                          humanize.naturalsize(virt.cached),
                          humanize.naturalsize(virt.available)))
    print(TEMPLATE.format('Swap:', humanize.naturalsize(swap.total),
                          humanize.naturalsize(swap.used),
                          humanize.naturalsize(swap.free),
                          '', '', '', ''))
