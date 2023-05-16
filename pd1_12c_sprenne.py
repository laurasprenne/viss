# Klase MyPoint, kas implementē sekojošo:
# konstruktors, kur tiek padots punkta x un y
# Funkcijas setX, setY, getXY, moveRight(d), moveLeft(d),
# moveUp(d), moveDown(d), distanceTo(point)
# Nodrošināt funkcionalitāti tā, lai punktu nebūtu iespējams
# pārvietot tālāk par 100 vienībām uz jebkuru pusi no
# _sākotnējās_ pozīcijas
# izveidot MyPoint objektu, nodemonstrēt vismaz četru
# iekšējo funkciju darbību

import math

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getXY(self):
        return[self.x, self.y]

    def moveRight(self, d):
        x = self.x + d 
        return[x, self.y]
    
    def moveLeft(self, d):
        x = self.x - d
        return[x, self.y]
    

    def moveUp(self, d):
        y = self.y + d
        return[self.x, y]
    

    def moveDown(self, d):
        y = self.y - d
        return[self.x, y]

    def distanceTo(self, point):
        x1 = self.getXY()[0]
        y1 = self.getXY()[1]

        x2 = point.getXY()[0]
        y2 = point.getXY()[1]

        x = x2 - x1
        y = y2 - y1

        return math.sqrt(x**2 + y**2)

p1 = MyPoint(4, 7)
p2 = MyPoint(5, 10)
print(p1.moveRight(5))
print(p1.moveLeft(4))
print(p1.moveUp(2))
print(p1.moveDown(10))
print(p1.distanceTo(p2))
    
# Klase Circle, kas par centra punktu izmanto MyPoint klases objektu
# implementē visas funkcijas, kas raksturīgas riņķa līnijai
# konstruktorā MyPoint objekts un rādiuss

class Circle:
    def __init__(self, r, circle):
        self.r = r
        self.center = center

    def getArea(self):
        return 3.14 * self.r**2

    def getCircumferance(self):
        return 3.14 * self.r * 2

    def overlap(self, circle):
        if self.center.distanceTo(circle.center.r) > self.r + circle.r:
            return False
        else:
            return True
    
p1 = MyPoint(4, 2)
p2 = MyPoint(7, 7)

circle1 = Circle(4, p1)
circle2 = Circle(4, p2)
print(circle1.overlap(circle2))