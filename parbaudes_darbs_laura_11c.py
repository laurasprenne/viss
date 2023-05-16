class TaisnlenkaTrijsturis:
    def __init__(self, a, b):
        self.akatete = a
        self.bkatete = b

    def Perimetrs(self):
        return self.akatete + self.bkatete + ((self.akatete**2 + self.bkatete**2)**0.5)

    def Laukums(self):
        return self.akatete * self.bkatete / 2

class Trapece:
    def __init__(self, a, b, h):
        self.pamats1 = a
        self.pamats2 = b
        self.augstums = h

    def Viduslinija(self):
        return (self.pamats1 + self.pamats2 )/2

    def Laukums(self):
        return self.Viduslinija() * self.augstums

class ToDoList:
    def __init__(self, a):
        self.darbi = a

    def Check(self):
        if self.darbi > 0:
            return self.darbi - 1
        elif self.darbi == 0:
            print('All done!')

class Stunda:
    def __init__(self, a):
        self.stundas = a

    def Add(self, x):
        laiks = self.stundas + x
        if laiks > 24:
            return laiks % 24
        elif laiks <= 24:
            return laiks

