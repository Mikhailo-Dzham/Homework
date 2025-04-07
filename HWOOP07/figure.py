import math

#WIP
class Figure:
    #Перелік Тридешних класів
    _3D_CLASSES = {"Ball", "Triangularpyramid", "Quadrangularpyramid", "Rectangularparallelepiped", "Cone", "TriangularPrism"}

    def __init__(self):
        self.dim3d = self.__class__.__name__ in self._3D_CLASSES #Перевіряємо належність класа до тридешних


    def _dimention(self):
        return self.dim3d

    def _perimetr(self):
        if self.dim3d:
            if self.__class__.__name__ == "Circle":
                return self.r *= math.pi
            else:
                return sum(self.sides)

        else:
            return None

    def _squareSurface(self):
        return






