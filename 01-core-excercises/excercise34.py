# entry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def even_numbers(number_list: list) -> list:
#     even_list = []
#     for i in number_list:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list
#
#
# print(even_numbers(entry))

entry = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def even_list(numbers: list) -> list:
    return [number for number in numbers if number % 2 == 0]


print(even_list(entry))
