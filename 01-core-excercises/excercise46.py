class ARN:
    ADENINE = "A"
    GUAINE = "G"
    CYTOSINE = "C"
    THYMINE = "T"

    def __init__(self, seq: str):
        self.seq = seq

    def __str__(self) -> str:
        return self.seq

    def __add__(self, other):
        seq = [max(b1, b2) for b1, b2 in zip(self.seq, other.seq)]
        return ARN("".join(seq))

    def __mul__(self, other):
        seq = [b1 if b1 == b2 else "_" for b1, b2 in zip(self.seq, other.seq)]
        return ARN("".join(seq))

    @property
    def size(self) -> int:
        return len(self.seq)

    @property
    def num_nucleotides(self) -> dict:
        return {nucleotide: self.seq.count(nucleotide) for nucleotide in
                (self.ADENINE, self.GUAINE, self.CYTOSINE, self.THYMINE)}

    @property
    def rate_nucleotides(self) -> dict:
        nucleotides = self.num_nucleotides
        return {nucleotide: round(nucleotides[nucleotide] / self.size, 2) for
                nucleotide in nucleotides}

    @property
    def num_adenine(self) -> int:
        return self.seq.count(self.ADENINE)

    @property
    def num_guaine(self) -> int:
        return self.seq.count(self.GUAINE)

    @property
    def num_cytosine(self) -> int:
        return self.seq.count(self.CYTOSINE)

    @property
    def num_thymine(self) -> int:
        return self.seq.count(self.THYMINE)


adn1 = ARN("ATGCGATACGCTTGA")
adn2 = ARN("AACGATAGCGGTATC")
adn3 = adn1 + adn2
adn4 = adn1 * adn2
print(adn3)
print(adn4)
print(adn1.num_nucleotides)
print(adn1.rate_nucleotides)
