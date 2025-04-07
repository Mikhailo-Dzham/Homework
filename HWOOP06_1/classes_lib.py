import numpy


class Matrix2D:
    def __init__(self, coefs):
        try:
            assert len(coefs) == 4
            self.matrix = [
                [coefs[0], coefs[1]],
                [coefs[2], coefs[3]]
            ]
        except AssertionError:
            print("В квадратній матриці повинно бути 4 елемента")

    def det(self):
        return round(numpy.linalg.det(numpy.array(self.matrix)), 2)
