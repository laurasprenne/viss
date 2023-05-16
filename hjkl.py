# class Taisnsturis:
#     def __init__(self, a, b):
#         self.mala1 = a
#         self.mala2 = b

#     def laukums(self):
#         return self.mala1 * self.mala2

#     def perimetrs(self):
#         return (a*2) + (b*2)

    




# a = int(input('Ievadi malu 1: '))
# b= int(input('Ievadi malu 2: '))

# t = Taisnsturis(a, b)

# print(t.laukums())
# print(t.perimetrs())

# class Person:
#     def __init__(self, n, surname, height, age):
#         self.name = n
#         self.surname = surname
#         self.height = height
#         self.age = age

#     def fullname():
#         return self.name + "" + self.surname

#     laura = Person("Laura", "Sprenne", 171, 17) 

#     print(laura.fullname())


# class Datums:
#     def __init__(self, d, m):
#         if d < 1  or d > 31:
#             print('datums nav pareizs')
#             self.day = 1
#         else:
#             self.day = d

#         if m < 1  or m > 12:
#             print('mesnesis nav pareizs')
#             self.month = 1
#         else:
#             self.month = m

#     def fullDate(self):
#         return str(self.day)  + "/" + str(self.month)

#     def nextDay(self):
#         if self.month == 2:
#             if self.day == 28:
#                 self.month += 1
#             else:
#                 self.day += 1

#         elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
#             if self.day == 30:
#                 self.month += 1
#             else:
#                 self.day += 1

#         else:
#             if self.day == 31:
#                 if self.month == 12:
#                     self.day =1
#                     self.month = 1
#                 else:
#                     self.month += 1
#                     self.day += 1
#             else:
#                 self.day += 1

# a = Datums(30, 2)
# print(a.fullDate())
# a.nextDay()
# print(a.fullDate())
# a.nextDay()
# print(a.fullDate())

# class Laiks:
#     def __init__(self, m, s):
#         self.minutes = m
#         if s < 1 or s > 59:
#             print('nepareizs laiks')
#             self.sekundes = 1
#         else:
#             self.sekundes = s

#     def nextSecond(self):
#         if self.sekundes < 59:
#             self.sekundes += 1
#         else:
#             self.sekundes = 0 
#             self.minutes += 1

#     def printLaiks(self):
#         if self.sekundes < 10:
#             return str(self.minutes)+ ":0"+ str(self.sekundes)
#         else:
#             return str(self.minutes)+ ":"+ str(self.sekundes)

# laiks = Laiks(3, 58)
# print(laiks.printLaiks())
# laiks.nextSecond()
# print(laiks.printLaiks())
# laiks.nextSecond()
# print(laiks.printLaiks())


# class subscription:
#     def __init__(self, p,):
#         self.price = p

#     def monthly(self, month_count):
#         return self.price*month_count

# spotify = subscription(6.99)
# print(spotify.monthly(12))

# class SekmjuIzraksts:
#     def __innit__(self):
#         self.sekmes = []

#     def atzime(self,a):
#         if a >= 1 and a <= 10:
#             self.sekmes.append(a)
#         else:
#             print("nepareiza atzīme")

#     def videjais(self):
#         return self.sekmes.avre 


        
# class Kvadratvienadojums: 
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def diskriminants(self):
#         return self.b**2 - (4 * self.a * self.c)

#     def sakne1(self):
#         if self.diskriminants() >= 0:
#             return (-self.b + self.diskriminants()**0.5)/self.a * 2

#     def sakne2(self):
#         if self.diskriminants() >= 0:
#             return (-self.b - self.diskriminants()**0.5)/self.a * 2

#     def xvirsotne(self):
#         return -self.b/(2*self.a)

#     def yvirsotne(self):
#         return self.a * self.xvirsotne()**2 + self.b + self.xvirsotne()

# vienadojums = Kvadratvienadojums(4, 6, 2)
# print('D =', vienadojums.diskriminants())
# print('x1 =', vienadojums.sakne1())
# print('x2 =', vienadojums.sakne2())
# print('parabolas virsotne = ', vienadojums.xvirsotne(), ',', vienadojums.yvirsotne())

# class Dziesma:
#     def __init__(self, nosaukums, izpilditajs, albums, garums):
#         self.title = nosaukums
#         self.artist = izpilditajs
#         self.album = albums
#         self.lenght = garums

#     def print1(self):
#         print(self.artist, '-', self.title)

#     def print2(self):
#         print(self.title, '-', self.lenght)

#     def print3(self):
#         print(self.album, '-', self.artist)
        
# muzika = Dziesma('Afraid', 'The neighbourhood', 'I LOVE YOU.', '2:26')

# muzika.print1()
# muzika.print2()
# muzika.print3()

# class Tprizma:
#     def __init__ (self, a, b, c, h):
#         self.mala1 = a
#         self.mala2 = b
#         self.mala3 = c
#         self.height = h

#     def pamatalaukums(self):
#         p = (self.mala1 + self.mala2 + self.mala3)/2
#         return (p*(p-self.mala1)*(p-self.mala2)*(p-self.mala3))**0.5

#     def tilpums(self):
#         return self.pamatalaukums() * self.height

#     def sanuvirsmas(self):
#         return (self.height * self.mala1) + (self.height * self.mala2) + (self.height * self.mala3)




# prizma = Tprizma(3, 4, 5, 7)
# print(prizma.pamatalaukums())
# print(prizma.tilpums())
# print(prizma.sanuvirsmas())

class Paralelskaldnis:
    def __init__(self, a, b, c):
        self.mala1 = a
        self.mala2 = b
        self.mala3 = c
    
    def Tilpums(self):
        return self.mala1*self.mala2*self.mala3

    def VirsmasS(self):
        return 2*(self.mala1*self.mala2 + self.mala2*self.mala3 + self.mala3*self.mala1)

    def Diognale(self):
        return (self.mala1**2 + self.mala2**2 +self.mala3**2)**0.5

paralelskaldnis = Paralelskaldnis(3, 4, 6)
print(paralelskaldnis.Tilpums())
print(paralelskaldnis.VirsmasS())
print(paralelskaldnis.Diognale())