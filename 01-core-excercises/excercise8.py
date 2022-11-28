vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü']
vowels_in_word = 0
word = input("Introduce una palabra: ")
word = word.lower()
for letter in word:
    if letter in vowels:
        vowels_in_word += 1
print(len(word) * vowels_in_word)
