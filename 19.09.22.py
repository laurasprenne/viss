import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
        
    def getXY(self):
        return[self.x, self.y]

    def distanceTo(self, point):
        x1 = self.getXY()[0]
        y1 = self.getXY()[1]

        x2 = point.getXY()[0]
        y2 = point.getXY()[1]

        x = x2 - x1
        y = y2 - y1

        return math.sqrt(x**2 + y**2)

p1 = Point(4, 7)
p2 = Point(5, 10)
print(p1.distanceTo(p2))

def isTaisnlenka(a, b, c):
    if a**2 == math.sqrt(b**2 + c**2) or b**2 == math.sqrt(a**2 + c**2) or c**2 == math.sqrt(b**2 + a**2):
        return True
    else:
        return False

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        mala1 = self.p1.distanceTo(self.p2)
        mala2 = self.p1.distanceTo(self.p3)
        mala3 = self.p3.distanceTo(self.p2)
        return mala1 + mala2 + mala3

    def surface(self):
        mala1 = self.p1.distanceTo(self.p2)
        mala2 = self.p1.distanceTo(self.p3)
        mala3 = self.p3.distanceTo(self.p2)
        p = self.perimeter()/2
        s = (p*(p-mala1)*(p-mala2)*(p-mala3))**0.5
        return s

    def getType(self):
        mala1 = self.p1.distanceTo(self.p2)
        mala2 = self.p1.distanceTo(self.p3)
        mala3 = self.p3.distanceTo(self.p2)

        if mala1 == mala2 == mala3:
            return "regulārs"
        elif mala1 == mala2 or mala1 == mala3 or mala2 == mala3:
            if isTaisnlenka(mala1, mala2, mala3):
                return "taisnleņķa vienādsānu"
            else:
                return "vienādsānu"
        else:
            if isTaisnlenka(mala1, mala2, mala3):
                return "tainleņķa dažādmalu"
            else:
                return "dažādmalu"

t1 = Point(3, 5)
t2 = Point(3, 8)
t3 = Point(-7, 2)

tri = Triangle(t1, t2, t3)
print(tri.perimeter())
print(tri.surface())
print(tri.getType())