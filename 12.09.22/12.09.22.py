# class Circle:
#     def __init__(self, radius, color="white"):
#         self.radius = radius
#         set.color = color
    
#     def getRadius(self):
#         return self.radius

#     def setRadius(self, r):
#         self.radius = r

#     def getArea(self):
#         return self.radius ** 2 * 3.14159265

#     def getCircumference(self):
#         return 2 * self.radius * 3.14159265

#     def toString(self):
#         return str(self.getRadius()) + " " + str(self.getCircumference())

# circle1 = Circle(5)
# print(circle1.getRadius())
# print(circle1.getCircumference())


# class Employee:
#     def __init__(self, id, name, surname, salary):
#         self.id = id
#         self.name = name
#         self.surname = surname
#         self.salary = salary

#     def getID(self):
#         return self.id

#     def getName(self):
#         return self.name + " " + self.surname

#     def getAnnualSalary(self):
#         return self.salary * 12

#     def riseSalary(self, perc):
#         self.salary *= (perc/100 + 1)

    
# john = Employee(15, "John", "Oates", 1400)
# print(john.getName())
# john.raiseSalary(10)

# class InvoiceItem():
#     def __init__(self, name, price, qty = 1):
#         self.name = name
#         self.price = price
#         self.qty = qty
    
#     def setQty(self, qty):
#         self.qty = qty

#     def getTotal(self):
#         return round(self.price * self.qty, 2)

#     def toString(self):
#         return str(self.qty) + " " + str(self.name) + " costs $" + str(self.price)

# apple = InvoiceItem("apple", 0.23)
# apple.setQty(5)
# print(apple.toString())

# class BankAccount():
#     def __init__(self, id, name, balance = 0):
#         self.id = id
#         self.name = name
#         self.balance = balance

#     def getID(self):
#         return self.id

#     def getName(self):
#         return self.name
    
#     def getBalance(self):
#         return self.balance

#     def credit(self, amount):
#         self.balance += amount

#     def transferTo(self, account, amount):
#         if amount <= self.getBalance():
#             self.balance -= amount
#             account.credit(amount)
#         else: print("Account", self.getID(), "has insufficient funds", sep=" ")

# account1 = BankAccount(21, "Laura Sprenne", 130)
# account2 = BankAccount(51, "Kārlis Zvejnieks", 160)

# print(account1.getBalance())
# print(account2.getBalance())
# account1.transferTo(account2, 140)

# print(account1.getBalance())
# print(account2.getBalance())

# def isLeapYear(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False

from re import S


def formatSingleDigit(d):
    if d < 10:
        return "0" + str(d)
    else:
        return str(d)

# class Date:
#     def __init__(self, d, m, y):
#         if [4, 6, 9, 11].count(m):
#             if d > 0 and d < 31:
#                 self.d = d
#                 self.m = m
#                 self.y = y
#             else:
#                 print("invalid input")
#                 self.d = 1
#                 self.m = m
#                 self.y = y
#         elif m == 2:
#             if isLeapYear(y) and d > 0 and d < 30:
#                 self.d = d
#                 self.m = m
#                 self.y = y
#             elif (not isLeapYear(y)) and d > 0 and d < 29:
#                 self.d = d
#                 self.m = m
#                 self.y = y
#             else:
#                 print("invalid input")
#                 self.d = 1
#                 self.m = m
#                 self.y = y
#         else:
#             if d > 0 and d < 32 and [1, 3, 5, 7, 8, 10, 12].count(m):
#                 self.d = d
#                 self.m = m
#                 self.y = y
#             else:
#                 print("invalid input")
#                 self.d = 1
#                 self.m = m
#                 self.y = y
#     def toString(self):
#         return formatDate(self.d) + "/" + formatDate(self.m) + "/" + str(self.y)

# x = Date(29, 3, 2001)
# print(x.toString())

# class Time:
#     def __init__(self, h, m, s):
#         if h >= 0 and h <= 23:
#             self.h = h
#         else:
#             print("invalid input")
#             self.h = 0
#         if m >= 0 and m <= 59:
#             self.m = m
#         else:
#             print("invalid input")
#             self.m = 0
#         if s >= 0 and s <= 59:
#             self.s = s
#         else:
#             print("invalid input")
#             self.s = 0

#     def toString(self):
#         return formatSingleDigit(self.h) + ":" + formatSingleDigit(self.m) + ":" + formatSingleDigit(self.s)

#     def addTime(self, time):
#         print(self.toString(), time.toString())
#         seconds = self.s + time.s
#         minutes = self.m + time.m
#         hours = self.h + time.h

#         if seconds > 59:
#             minutes +=1
#             seconds = seconds % 60
#         if minutes > 59:
#             hours += 1
#             minutes = minutes % 60
#         if hours > 23:
#             hours = hours % 24

#         self.s = seconds
#         self.m = minutes
#         self.h = hours

# n = Time(22, 45, 00)
# m = Time(4, 54, 10)
# n.addTime(m)

# print(n.toString())
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
