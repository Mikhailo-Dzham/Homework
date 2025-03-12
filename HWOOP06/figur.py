import math
from math import pi


class Circle:
    longest_cir = 0
    biggest_cir_area = 0

    def __init__(self, r):
        self.r = r
        self.len = round((2 * r * pi), 3)
        self.area = round((pi * r ** 2), 3)
        Circle.biggest_cir_area = round(max(Circle.biggest_cir_area, self.area), 3)
        Circle.longest_cir = round(max(Circle.longest_cir, self.len), 3)


class Rectangle:
    max_p = 0
    max_area = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.p = 2 * (self.a + self.b)
        self.area = self.a * self.b
        Rectangle.max_p = round(max(Rectangle.max_p, self.p), 3)
        Rectangle.max_area = round(max(Rectangle.max_area, self.area), 3)


class Trapeze:
    max_p = 0
    max_area = 0

    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.p = self.a + self.b + self.c + self.d
        Trapeze.max_p = round(max(Trapeze.max_p, self.p), 3)

        if self.is_valid_trapeze():
            s = self.p / 2
            try:
                if (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d) >= 0:
                    self.area = ((self.a + self.b) / abs(self.a - self.c)) * (
                        (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d)) ** 0.5
                    Trapeze.max_area = round(max(Trapeze.max_area, self.area), 3)
                    print("ok")
                else:
                    self.area = 0
            except ValueError:
                self.area = 0  # Якщо під коренем від'ємне значення
        else:
            self.area = 0  # Якщо трапеція не існує
        

    def is_valid_trapeze(self):
        return (self.a + self.b + self.c > self.d and
                self.a + self.b + self.d > self.c and
                self.a + self.c + self.d > self.b and
                self.b + self.c + self.d > self.a)

class Triangle:
    max_p = 0
    max_area = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if (self.a + self.b + self.c - max(self.a, self.b, self.c)) >= max(self.a, self.b, self.c):
            self.p = self.a + self.c + self.b
            self.area = ((self.p / 2) * (self.p / 2 - self.a) * (self.p / 2 - self.b) * (self.p / 2 - self.c)) ** 0.5
            Triangle.max_p = round(max(Triangle.max_p, self.p), 3)
            Triangle.max_area = round(max(Triangle.max_area, self.area), 3)


class Parallelogram:
    max_p = 0
    max_area = 0

    def __init__(self, a, b, k):
        self.a = a
        self.b = b
        self.k = k
        self.p = 2 * (self.a + self.b)
        self.area = self.a * self.b * (math.sin(math.radians(self.k)))
        Parallelogram.max_p = round(max(Parallelogram.max_p, self.p), 3)
        Parallelogram.max_area = round(max(Parallelogram.max_area, self.area), 3)


if __name__ == '__main__':
    pass
