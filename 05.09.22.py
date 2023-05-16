# s = int(input("ievadi skaitli: "))
# if s > 10:
#     print("lielaks")
# elif s == 10:
#     print("vienads")
# else:
#     print("mazaks")

# #while
# x = int(input("ievadi skaitli: "))
# while x != 0:
#     x = int(input("ievadi skaitli: "))

# #for
# for i in range(1, 21, 2):
#     print(i)

# for i in range(21):
#     if i % 2 != 0:
#         print(i)

# #masīvi
# m = [1, 4, 2, 7, 3]

# for i in range(len(m)):
#     print(m[i])

# #divdimensiju masivs
# dd = [[1, 4, 2, 7, 3],
#       [1, 4, 2, 7, 3],
#       [1, 4, 2, 7, 3],
#       [1, 4, 2, 7, 3],
#       [1, 4, 2, 7, 3]]

# print(dd[3][2])

#simbolu virknes

# teikums = "Labrīt,  Deivid! "
# print(len(teikums))
# print(teikums.count("") + 1)

# vardi = teikums.split(" ")
# print(vardi)

# jauns = []
# for vards in vardi:
#     if len(vards) > 0:
#         jauns.append(vards)

# print(jauns)

# text = "TukumaRainaValstsGimnazija"

# for char in text:
#     if ord(char) > 64 and ord(char) < 91:
#         print(" ", end=" ")
#         print(char, end=" ")
#     else:
#         print(char, end=" ")

text = "tukuma raina valsts gimnazija"

c = chr(ord(text[1]) - 32)
i = 0
temp = 0
new = " "

while i < len(text):
    if temp == i:
        new += chr(ord(text[1]) - 32)
    elif text[i] == " ":
        temp = i + 1
        new += " "
    else:
        new += text[i]
    i += 1

print(new)