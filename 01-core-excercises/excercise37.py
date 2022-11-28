entry = "The quick brown fox jumps over the lazy dog"
entry2 = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña " \
         "tocaba el saxofón detrás del palenque de paja."
ALPHABET_ENG = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_ESP = "abcdefghijklmnñopqrstuvwxyz"


def remove_accents(quote: str) -> str:
    accents = "áéíóúü"
    no_accents = "aeiouu"
    for i in range(len(accents)):
        quote = quote.replace(accents[i], no_accents[i])
    return quote


def pangram(quote: str, alphabet: str) -> bool:
    quote = remove_accents(quote.lower())
    return set(quote) >= set(alphabet)


print(pangram(entry2, ALPHABET_ESP))

