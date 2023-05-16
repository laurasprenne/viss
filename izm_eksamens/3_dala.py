class Figura:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    class Kvadrats:
        def __init__(self, a):
            self.a = a
        def perimetrs(self):
            return a**2
    
mala = Figura(2, 0, 0)
print(mala.Kvadrats.perimetrs())
