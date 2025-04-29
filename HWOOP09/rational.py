class Rational:
    def __init__(self, n, d=None):
        if d:
            self.n = n
            self.d = d
        elif isinstance(n, str):
            self.n, self.d = [int(i) for i in n.split('/')]
        elif isinstance(n, Rational):
            self.n, self.d = n.n, n.d
        elif d is None and isinstance(n, int):
            self.n = n
            self.d = 1
        else:
            pass
        self.reduction()

    def __add__(self, other):
        oth = Rational(other)
        return Rational(self.n * oth.d + self.d * oth.n, self.d * oth.d)

    def __radd__(self, other):
        oth = Rational(other)
        return Rational(self.d * oth.n + self.n * oth.d, self.d * oth.d)

    def __sub__(self, other):
        oth = Rational(other)
        return Rational(self.n * oth.d - self.d * oth.n, self.d * oth.d)

    def __rsub__(self, other):
        oth = Rational(other)
        return Rational(self.d * oth.n - self.n * oth.d, self.d * oth.d)

    def __truediv__(self, other):
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

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, item):
        if item == 'd':
            return self.d
        else:
            return self.n

    def reduction(self):
        a = max(self.n, self.d)
        b = self.n + self.d - a
        while a % b != 0:
            a, b = b, a % b
        self.n //= b
        self.d //= b


class BadDenominator(Exception):
    pass
