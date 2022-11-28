import sys

# values_string = sys.argv[1:]
# values = [int(value) for value in values_string]
# average = sum(values) / len(values)
# print(f"{average:.2f}")

values = sys.argv[1:]
average = sum([int(value) for value in values]) / len(values)
print(f"{average:.2f}")

# values = sys.argv[1:]
# int_values = []
# for value in values:
#     int_values.append(int(value))
#
# average = sum(int_values) / len(int_values)
# print(f"{average:.2f}")
