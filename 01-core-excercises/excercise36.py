entry = "Ana lava lana"
entry2 = "hola a todos"


def palindrome(quote: str) -> bool:
    quote = quote.replace(" ", "").lower()
    return quote == quote[::-1]


print(palindrome(entry))
