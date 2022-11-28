from random import choice

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday']


def get_random_day():
    return choice(WEEKDAYS)


print(get_random_day())
