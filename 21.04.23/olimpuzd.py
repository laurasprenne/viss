m = []
a = 0
b = 0
m = []

with open("olimpuzd.txt") as f:
    lines = f.readlines()
    line1 = lines[0].split(" ")
    x, y, a, b = int(line1[0]), int(line1[1]), int(line1[2]), int(line1[3])
    
    for line in lines[1:]:
        row = []
        for num in line.split(" "):
            row.append(int(num))
        m.append(row)

print(m)

skaits = 0

def rectangleSum(i, j, h, v):
    sum = 0
    for ii in range(i, h + i):
        for jj in range(j, v + j):
            sum += m[ii][jj]
    return sum

def subArray(h, v):
    sums = []
    if h > x or v > y:
        return[]
    
    for i in range(x):
        for j in range(y):
            if x - i >= h and y - j >= v:
                sums.append(rectangleSum(i, j, h, v))
    return sums

    
    # sumArray = []
    # if h == 1 and v == 1:
    #     for row in m:
    #         for elem in row:
    #             sumArray.append(elem)

bigArray = []
for i in range(1, x + 1):
    for j in range(1, y + 1):
        bigArray.append(subArray(i, j))

sum = 0
for results in bigArray:
    for result in results:
        if a <= result <+ b:
            sum =+ 1

print(sum)
