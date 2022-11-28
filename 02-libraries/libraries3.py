import datetime

from pytz import timezone


#
# media_hora = datetime.timedelta(hours=0.5)
# nine_and_half_hours = datetime.timedelta(hours=9.5)
#
# print(nine_and_half_hours)

# COVID_19 = datetime.date(2020, 3, 11)
# today = datetime.date.today()
# days_since_covid = today - COVID_19
# print(days_since_covid.days, 'days since covid')
#
# yesterday = today - datetime.timedelta(days=1)


def get_difference_hours():
    spain = timezone('Europe/Madrid')
    canary_islands = timezone('Atlantic/Canary')
    london = timezone('Europe/London')
    spain_time = datetime.datetime.now(spain)
    canary_islands_time = datetime.datetime.now(canary_islands)
    london_time = datetime.datetime.now(london)
    print(spain_time)
    print(canary_islands_time)
    return london_time - spain_time


print(get_difference_hours())
