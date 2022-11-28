import arrow


def count_friday_13ths(year):
    count = 0
    for month in range(1, 13):
        if arrow.get(year, month, 13).weekday() == 4:
            count += 1
    return count


for year in range(2010, 2030):
    print(year, count_friday_13ths(year))
