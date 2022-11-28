def cycle_alphabet(max_letter: int = -1) -> str:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    i, num_letters, size = 0, 0, len(ALPHABET)
    while num_letters < max_letter or max_letter == -1:
        yield ALPHABET[i % size]
        i += 1
        num_letters += 1


# for letter in next_letter(15):
#     print(letter.join(" "))

print("".join(cycle_alphabet()))
