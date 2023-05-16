#1
# dic = {}

# for i in range(1, 11):
#     dic[i] = i**2

# 2
dic = {}
dic2 = {
    '3': '10',
    '6': '9',
    '9': '0'
    }

with open("dictionary1.txt") as f:
    lines = f.readlines()
    for line in lines:
        key_value = line.split()
        dic[key_value[0]] = key_value[1]

for key in dic:
    if dic[key] in dic2:
        print(key, dic2[dic[key]])

# with open("dictionary2.txt")as f:
#     line1 = f.readline()
#     vertibas = line1.split()

#     pSkaits = int(vertibas[0])
#     zPieturas = int(vertibas[1])
#     posmi = int(vertibas[2])

#     print(pSkaits, zPieturas, posmi)

#     pieturas = {i:[] for i in range(1,12)}
#     print(pieturas)

#     for _ in range(posmi):
#         line = f.readline()
#         line = line.split()
#         #iegust katras vertibas skaitlisko vertibu
#         #for i in range(len(line)):
#         #line[i] = int(line[i])
#         line[0] = int(line[0])
#         line[1] = int(line[1])

#         pieturas[line[0]].append(line[1])
#         pieturas[line[1]].append(line[0])

#     zalas = {}
#     sarkanas = {}

#     for key in pieturas:
#         if key > 7:
#             sarkanas[key] = pieturas[key]
#         else:
#             zalas[key] = pieturas[key]
            
#     print(zalas, sarkanas)

    