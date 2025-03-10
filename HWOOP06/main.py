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
