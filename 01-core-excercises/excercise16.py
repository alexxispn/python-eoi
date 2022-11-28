# fibonacci sequence
last_number = 0
current_number = 0
fibonacci_size = int(input("How many numbers do you want to see? "))

if current_number == 0:
    print(current_number)
    current_number = 1

for i in range(fibonacci_size - 1):
    print(current_number)
    current_number = current_number + last_number
    last_number = current_number - last_number
