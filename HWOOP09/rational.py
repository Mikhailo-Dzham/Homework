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

    def reduction(self):
        a = max(self.n, self.d)
        b = self.n + self.d - a
        while a % b != 0:
            a, b = b, a % b
        self. n //= b
        self.d //= b

class BadDenominator(Exception):
    pass
