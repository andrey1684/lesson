class Fraction:
    def __init__(self, num = 0, den = 1):
        if den == 0:
            raise ValueError("Zero division error")
        self.__num = num
        self.__den = den

    def __reduce(self):
        def gcd(num, den):
            if num == 0:
                return den
            elif den == 0:
                return num
            elif num >= den:
                return gcd(num % den, den)
            else:
                return gcd(num, den % num)
        sign = 1
        if (self.__num > 0 > self.__den) or (self.__num < 0 < self.__den):
            sign = -1
        num, den = abs(self.__num), abs(self.__den)
        common = gcd(num, den)
        self.__num = sign * (num // common)
        self.__den = den // common

    # def __clone(self):
    #     return self
    @property
    def numerator(self):
        return self.__num

    @numerator.setter
    def numerator(self, value):
        self.__num = int(value)

    @property
    def denominator(self):
        return self.__den

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError("Zero division error")
        self.__den = int(value)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            mulnam = self.__num * other.__num
            mulden = self.__den * other.__den
            return Fraction(mulnam, mulden)
        raise ValueError("Illegal type of the argument")

    def __add__(self, other):
        if isinstance(other, Fraction):
            addnum = self.__num * other.__den + other.__num * self.__den
            addden = self.__den * other.__den
            return Fraction(addnum, addden)
        else:
            raise ValueError("Illegal type of the argument")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            subnum = self.__num * other.__den - other.__num * self.__den
            subden = self.__den * other.__den
            return Fraction(subnum, subden)
        else:
            raise ValueError("Illegal type of the argument")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            self.__reduce()
            other.__reduce()
            return self.__num == other.__num and self.__den == other.__den
        else:
            return False

    def __float__(self):
        if self.__den == 0:
            raise ZeroDivisionError
        return self.__num / self.__den

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.__float__() > other.__float__()

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.__float__() < other.__float__()


    def __str__(self):
        return f"Fraction: {self.__num}, {self.__den}"



f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

