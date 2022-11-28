entry = int(input("Enter a number: "))


def fibonacci(n: int) -> int:
    return 1 if n == 0 else n * fibonacci(n - 1)


for i in range(1, entry + 1):
    print(f"{i}! = {fibonacci(i)}")
print(f"{entry}! = {fibonacci(entry)}")
