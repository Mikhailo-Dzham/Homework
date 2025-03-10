from math import pi

class Circle:
    longest_cir = 0
    biggest_cir_area = 0
    def __init__(self, r):
        self.r = r
        self.len = round((r * pi), 3)
        self.area = round((pi * r**2), 3)
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






if __name__ == '__main__':
    pass