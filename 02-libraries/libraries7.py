import calendar
import os


def make_year_dirs(year):
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            path = os.path.join(str(year), str(month), str(day))
            if not os.path.exists(path):
                os.makedirs(path)


def remove_year_dirs(year):
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            path = os.path.join(str(year), str(month), str(day))
            if os.path.exists(path):
                os.removedirs(path)


make_year_dirs(2023)
# remove_year_dirs(2023)
