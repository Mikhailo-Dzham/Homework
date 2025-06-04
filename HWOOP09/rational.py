from rat_exceptions import *

class Rational:
    def __init__(self, n, d=None):
        if  d == 0:
            raise RationalError()
        elif d: #When Rational(3, 4) or similar
            self.n = n
            self.d = d
        elif isinstance(n, str): #When Rational("3/4") or similar
            if "/" in n:
                self.n, self.d = [int(i) for i in n.split('/')]
            else:
                try:
                    n = float(n)
                    self.n, self.d = self._float_to_rat(n)
                except ValueError:
                    raise RationalValueError

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
        if self.d < 0:
            self.d = abs(self.d)
            self.n = - self.n


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

    def __truediv__(self, other): # R / O
        oth = Rational(other)
        return Rational(self.n * oth.d, self.d * oth.n)

    def __rtruediv__(self, other): # O / R
        oth = Rational(other)
        return Rational(self.d * oth.n, self.n * oth.d)

    def __mul__(self, other): # R * O
        oth = Rational(other)
        return Rational(self.n * oth.n, self.d * oth.d)

    def __rmul__(self, other): # O * R = R * O
        oth = Rational(other)
        return Rational(self.n * oth.n, self.d * oth.d)

    def __pow__(self, power, modulo=None): # R ** power
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
        if self.n == 0:
            self.d = 1
        else:
            a = max(self.n, self.d)
            b = self.n + self.d - a
            while a % b != 0:
                a, b = b, a % b
            self.n //= b
            self.d //= b




class RationalList(list):
    def __init__(self, iterable=None):
        super().__init__()
        if iterable:
            for item in iterable:
                self.append(self._ensure_rational(item))

    def _ensure_rational(self, value) -> Rational:
        if isinstance(value, Rational):
            return value
        try:
            return Rational(value)
        except Exception:
            raise RationalValueError(f"Invalid element for RationalList: {value}")

    def __getitem__(self, index):
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        value = self._ensure_rational(value)
        super().__setitem__(index, value)

    def __len__(self):
        return super().__len__()

    def __add__(self, other):
        result = RationalList(self)
        if isinstance(other, RationalList):
            for item in other:
                result.append(self._ensure_rational(item))
        else:
            result.append(self._ensure_rational(other))
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other:
                self.append(self._ensure_rational(item))
        else:
            self.append(self._ensure_rational(other))
        return self

    def append(self, value):
        value = self._ensure_rational(value)
        super().append(value)

    def __iter__(self):
        return iter(sorted(
            super().__iter__(),
            key=lambda r: (-r.d, -r.n)
        ))


class BadDenominator(Exception):
    pass
