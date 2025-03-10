from math import pi


class Circle:
    longest_cir = 0
    biggest_cir_area = 0

    def __init__(self, r):
        self.r = r
        self.len = round((r * pi), 3)
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
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.p = self.a + self.c + self.b + self.d
        #Формула Бахмадупти, головне шо праціє
        self.area = ((self.a + self.b) / (self.a - self.c)) * ((self.p / 2 - self.a) * (self.p / 2 - self.b) * (self.p / 2 - self.c) * (self.p / 2 - self.d))**0.5
        Trapeze.max_p = round(max(Trapeze.max_p, self.max_p), 3)
        Trapeze.max_area = round(max(Trapeze.max_area, self.max_area), 3)

class Triangle:
    max_p = 0
    max_area = 0
    def __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c
        self.p = self.a + self.c + self.b
        self.area = ((self.p/2) * (self.p / 2 - self.a) * (self.p / 2 - self.b) * (self.p / 2 - self.c))**0.5
        Triangle.max_p = round(max(Triangle.max_p, self.max_p), 3)
        Triangle.max_area = round(max(Triangle.max_area, self.area), 3)



if __name__ == '__main__':
    pass
