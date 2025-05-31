class Rational:
    def __init__(self, n, d=None):
        if d: #When Rational(3, 4) or similar
            self.n = n
            self.d = d
        elif isinstance(n, str): #When Rational("3/4") or similar
            self.n, self.d = [int(i) for i in n.split('/')]
        elif isinstance(n, Rational): #When Rational(Rational(x)) or similar
            self.n, self.d = n.n, n.d
        elif d is None and isinstance(n, int): #When Rational(3) or similar
            self.n = n
            self.d = 1
        elif isinstance(n, float): #When Rational(3.4) or similar
            self.n, self.d = self._float_to_rat(n)


        else:
            raise ValueError
        self.reduction()

    def _float_to_rat(self, n)->tuple:
        nl, nr = str(n).split(".")
        return int(nl + nr), int("1" + "0" * len(nr))


    def __add__(self, other): # R + O
        oth = Rational(other)
        return Rational(self.n * oth.d + self.d * oth.n, self.d * oth.d)

    def __radd__(self, other): # O + R
        oth = Rational(other)
        return Rational(self.d * oth.n + self.n * oth.d, self.d * oth.d)

    def __sub__(self, other): # R - O
        oth = Rational(other)
        return Rational(self.n * oth.d - self.d * oth.n, self.d * oth.d)

    def __rsub__(self, other): # O - R
        oth = Rational(other)
        return Rational(self.d * oth.n - self.n * oth.d, self.d * oth.d)

    def __truediv__(self, other): # R / 
        oth = Rational(other)
        return Rational(self.n * oth.d, self.d * oth.n)

    def __rtruediv__(self, other):
        oth = Rational(other)
        return Rational(self.d * oth.n, self.n * oth.d)

    def __mul__(self, other):
        oth = Rational(other)
        return Rational(self.n * oth.n, self.d * oth.d)

    def __rmul__(self, other):
        oth = Rational(other)
        return Rational(self.n * oth.n, self.d * oth.d)

    def __pow__(self, power, modulo=None):
        return Rational(self.n ** power, self.d ** power)

    def __call__(self)->float:
        return self.n / self.d

    def __getitem__(self, item):
        if item == 'd':
            return self.d
        else:
            return self.n

    def __str__(self):
        return f"{self.n}/{self.d}"

    def reduction(self):
        a = max(self.n, self.d)
        b = self.n + self.d - a
        while a % b != 0:
            a, b = b, a % b
        self.n //= b
        self.d //= b

class RationalList(list):

    def __init__(self):
        super().__init__()


    def _ensure_rational(self, value)->Rational:
        if isinstance(value, Rational):
            return value
        try:
            return Rational(value)
        except Exception:
            raise TypeError(f"Elements must be Rational or convertible: got {value}")

class BadDenominator(Exception):
    pass
