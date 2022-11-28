date = "12/31/20"
[month, day, year] = date.split("/")
formatted_date = [day, month, "20" + year]
formatted_date = "-".join(formatted_date)
print(formatted_date)
