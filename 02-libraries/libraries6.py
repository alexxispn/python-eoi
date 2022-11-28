import os

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday']


def make_dirs():
    [os.mkdir(day) for day in WEEKDAYS if not os.path.exists(day)]


def remove_dirs():
    [os.rmdir(day) for day in WEEKDAYS if os.path.exists(day)]

# make_dirs()
# remove_dirs()
