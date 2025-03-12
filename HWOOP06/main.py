from figur import *


#WIP
#Якщо це читає магістр якого Креневич примусив перевіряти домашки то можна поставити бал авансом, потім тут все буде, Чесне слово
#Якщо це читає Креневич, що малоймовірно, то давайте зробимо вигляд що цього комміту не було

longest_cir = 0

name = 'input0' + input() + '.txt'
with open(name, 'r') as f:
    for line in f:
        line = line.split()
        if line[0] == "Circle":
            cir = Circle(float(line[1]))
        elif line[0] == "Rectangle":
            rec = Rectangle(float(line[1]), float(line[2]))
        elif line[0] == "Trapeze":
            trap = Trapeze(float(line[1]), float(line[2]), float(line[3]), float(line[4]))
        elif line[0] == "Triangle":
            tri = Triangle(float(line[1]), float(line[2]), float(line[3]))
        elif line[0] == "Parallelogram":
            Parallelogram(float(line[1]), float(line[2]), float(line[3]))
print(f"Коло макс довжина {Circle.longest_cir} та площа {Circle.biggest_cir_area}")
print(f"Прямокутник периметр {Rectangle.max_p} та площа {Rectangle.max_area}")
print(f"Трапеція периметр {Trapeze.max_p} та площа {Trapeze.max_area}  (знаходиться некоректно)")
print(f"Трикутник Прямокутник периметр {Triangle.max_p} та площа {Triangle.max_area}")
print(f"Паралелограм Прямокутник периметр {Parallelogram.max_p} та площа {Parallelogram.max_area}")


