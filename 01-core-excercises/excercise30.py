# average_month_temps = []
# with open('./temperatures.txt', 'r') as f:
#     for month in f:
#         total_month_temp = 0
#         days_month = month.split(',')
#         for day in days_month:
#             total_month_temp += int(day)
#         average_month_temps.append(total_month_temp / len(days_month))
#
# with open('./avgtemps.txt', 'w') as f:
#     for average_month_temp in average_month_temps:
#         f.write(f'{average_month_temp}\n')

average_temp_months = []
with open('./temperatures.txt', 'r') as f:
    for month in f:
        days_month = month.split(',')
        average_temp_month = sum([int(day) for day in days_month]) / len(
            days_month)
        average_temp_months.append(average_temp_month)

with open('./avgtemps.txt', 'w') as f:
    for average_temp_month in average_temp_months:
        f.write(f'{average_temp_month}\n')
