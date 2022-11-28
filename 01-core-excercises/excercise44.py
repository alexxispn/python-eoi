class Fraction:
    def __init__(self, num: int, den: int):
        gcd = Fraction.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, fraction):
        num = self.num * fraction.den + self.den * fraction.num
        den = self.den * fraction.den
        return Fraction(num, den)

    def __sub__(self, fraction):
        num = self.num * fraction.den - self.den * fraction.num
        den = self.den * fraction.den
        return Fraction(num, den)

    def __mul__(self, fraction):
        num = self.num * fraction.num
        den = self.den * fraction.den
        return Fraction(num, den)

    def __floordiv__(self, fraction):
        num = self.num * fraction.den
        den = self.den * fraction.num
        return Fraction(num, den)

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b > 0:
            a, b = b, a % b
        return a


eq1 = Fraction(25, 30)
eq2 = Fraction(40, 45)
eq3 = eq1 + eq2
eq4 = eq1 - eq2
eq5 = eq1 * eq2
eq6 = eq1 // eq2
print(f'{eq3}\n{eq4}\n{eq5}\n{eq6}')
