import numpy as np


class Matrix2D:
    def __init__(self, coefs):
        try:
            assert len(coefs) == 4
            self.matrix = [
                [coefs[0], coefs[1]],
                [coefs[2], coefs[3]]
            ]
        except AssertionError:
            print("У квадратній матриці повинно бути 4 елементи")
            self.matrix = None

    def det(self):
        if self.matrix is not None:
            return round(np.linalg.det(np.array(self.matrix)), 2)
        else:
            return None

    def show(self):
        if self.matrix is not None:
            print("Матриця:")
            for row in self.matrix:
                print(row)
            print("Визначник:", self.det())
        else:
            print("Матриця не ініціалізована.")

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(a[0][0])
det = numpy.linalg.det(numpy.array(a))
print(det)

b = (1, 2, 3, 4)
mb = Matrix2D(b)
print(mb.det())