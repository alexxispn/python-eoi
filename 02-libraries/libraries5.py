import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)


def func():
    log.debug('A debug message')
    log.info('An info message')
    log.warning('A warning message')
    log.error('An error message')
    log.critical('A critical error message')


if __name__ == '__main__':
    func()
