entry = {"Juan": 5, "Antonio": 5, "Inma": 4, "Esteban": 5}
history = []
# entry = list(entry.values())
# if entry.count(entry[0]) == len(entry):
#     print("Same values")
# else:
#     print("Not same values")

# for value in entry.values():
#     if value not in history:
#         history.append(value)
# if len(history) == 1:
#     print("Same values")
# else:
#     print("Not same values")

dict.fromkeys(entry.values())
if len(dict.fromkeys(entry.values())) == 1:
    print("Same values")
else:
    print("Not same values")
