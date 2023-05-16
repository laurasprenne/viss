#1
# x = int(input("Ievadi X skaitli: "))
# y = int(input("Ievadi Y skaitli: "))

# if x > y:
#     print(x-y)
# else:
#     print(y-x)

#2
# x = int(input("Ievadi X skaitli: "))

# if a%2 == 0:
#     print(a, " ir pāra skaitlis")
# else:
#     print(a, "ir nepāra skaitlis")

#3
# x = int(input("Ievadi X skaitli: "))
# y = int(input("Ievadi Y skaitli: "))

# if x > 0 and y > 0:
#     print("punkts atrodas 1. kvadrantā")
# elif x < 0 and y > 0:
#     print("punkts atrodas 2. kvadrantā")
# elif x < 0 and y < 0:
#     print("punkts atrodas 3. kvadrantā")
# else:
#     print("punkts atrodas 4. kvadrantā")

#4
# x = int(input("Ievadi trīscipara skaitli"))
# a = x%10
# b = ((x-a)/10)%10
# c = (x-a-10*b)/100
# print("šo ciparu summa ir: "a+b+c)

#5
# a = int(input("Ievadi 1. skaitli: "))
# b = int(input("Ievadi 2. skaitli: "))
# c = int(input("Ievadi 3. skaitli: "))

# if a > b and a > c:
#     if b > c:
#         print(c, b, a)
#     else:
#         print(b, c, a)
# elif b > a and b > c:
#     if a > c:
#         print(c, a, b)
#     else:
#         print(a, c, b)
# else:
#     if a > b:
#         print(b, a, c)
#     else:
#         print(a, b, c)

#6
# a = int(input("Ievadi mēnesi: "))
# b = int(input("Ievadi dienu: "))

# if a == 4 or a == 6 or a == 9 or a == 11:
#     if b > 30:
#         print("Datums neeksistē!")
#     else:
#         print("Datums eksistē!")
# elif a == 2 and b > 28:
#     print("Datums neeksistē!")
# elif b > 31 or a > 12:
#     print("Datums neeksistē!")

#7
# a = int(input("Ievadi 1. skaitli: "))
# b = int(input("Ievadi 2. skaitli: "))
# c = int(input("Ievadi 3. skaitli: "))
# summa = 0

# if a%2 == 0:
#     summa += a
# if b%2 == 0:
#     summa += b
# if c%2 == 0:
#     summa += c

# print(summa)    

#9
# n = input("ievadi divciparu skaitli: ")

# n_reversed = n[::-1]
# print(int(n)) + int(n_reversed)

#14
# n = int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

#15
# n = int(input("n: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

#16
# a = int(input("Ievadi skaitli: "))
# summa = 0
# while a != 0:
#    summa += a
#    a = int(input("Ievadi skaitli: "))
# print(summa)

#17
# n = int(input("n: "))
# i = 1
# while i <= n:
#     print(i)
#     i = i + 1

#18
# n = int(input("n: "))
# for i in range(n + 1):
#     print(i**2)

#19
# n = int(input("n: "))
# i = 1
# while i * i < n:
#     print(i * i)

#20
# n = int(input("n: "))
# i = 2*n
# while n < i:
#     n += 1
#     print(n)

#21


#27
# n = int(input("n: "))
# while n != 0:
#     n = int(input("n: "))
#     if m > n:
#         print("lielaks")
#     else:
#         print("nav lielaks")
#     n = m

#30
# atzimes = []
# for i  in range(7):
#     row = []
#     atz = int(input("ievadi atzimi " + str(i+1) + ". skolēnam"))
#     while atz != 0:
#         row.append(row)
#         atz = int(input("ievadi atzimi " + str(i+1) + ". skolēnam"))
#     atzimes.append(row)

#41
# m = [1, 5, 3, 7, 2, 4, 2, 7, 9, 2, 5, 6]
# diction = {}
# for num in m:
#     diction[num] = m.count(num)
# print(diction)

# sorted_list = sorted(diction, key=diction.get)
# print(sorted_list[-1])

#44
# m = [1, 5, 3, 7, 2, 4, 2, 7, 9, 2, 5, 6]
# m_copy = []

# for elem in m:
#     if m_copy.count(elem) < 1:
#         m_copy.append(elem)

# print(m_copy)
# print(list(set(m)))

#45
# text = "The Serbian tennis star was detained in January over his refusal to be vaccinated against Covid. He was deported from the country 10 days later, despite mounting a successful legal challenge. At times dubbed Fortress Australia, the country had some of the strictest pandemic restrictions in the world. When Djokovic arrived in Australia in January, Covid cases were skyrocketing and government rules required anyone entering the country be vaccinated, unless they had a valid medication exemption."
# text = text.lower()
# text = text.replace(".", "").replace(",", "").replace("!", "").replace(" ", "")
# d = {}

# import string
# for char in string.ascii_lowercase:
#     d[char] = round(text.count(char) / len(text) * 100, 2)

# for key in d:
#     print(key, d[key])
#68
# def printArray(m):
#     for row in m:
#         for elem in row:
#             print(elem, end=" ")
#         print()
        
# import random

# chess = [[0 for _ in range(8)] for _ in range(8)]
# chess[random.randint(0,7)][random.randint(0,7)] = 1
# chess[random.randint(0,7)][random.randint(0,7)] = 1
# arr = [[0 for _ in range(8)] for _ in range(8)]


# burts = "abcdefgh"
# poz = input("pozicija: ")
# y = burts.index(poz[0])
# x = 8 - int(poz[1])
# arr[x][y] = 1
# printArray(arr)

#69
#a) tornis
# for i in range(8):
#     for j in range(8):
#         if i == x or j == y:
#             arr[i][j] += 1
#b) laidnis
# for i in range(8):
#     for j in range(8):
#         if i + j == x + y or i - j ==  x- y:
#             arr[i][j] += 1
#c) dāma
# for i in range(8):
#     for j in range(8):
#         if i+j == x+y or i-j == x-y or i == x or j == y:
#             arr[i][j] +=1

#d) karalis
# for i in range(8):
#     for j in range(8):
#         if abs(x-i) <= 1 and abs(y-j) <= 1:
#             arr[i][j] +=1

#e) zirgs
# for i in range(8):
#     for j in range(8):
#         if (abs(x-i) == 1 and abs(y-j) == 2) or (abs(x-i) == 2 and abs(y-j) == 1):
#             arr[i][j] +=1


# printArray(arr)

#70
# mas = [2, 5, 7, 2, 7, 1, 4, 9, 2]
# mas2d = []
# index = 0

# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(mas[index])
#         index += 1
#     mas2d.append(row)

# printArray(mas2d)