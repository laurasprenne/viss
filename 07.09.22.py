from re import M


def summa(n):
    sum = 0
    while n > 0:
        sk = n % 10
        n = (n - sk) // 10
        sum =+ sk

    return sum

def otradi(n):
    sum = 0
    while n > 0:
        sk = n % 10
        n = (n - sk) // 10
        sum = sum * 10 + sk

    return otradi

print(otradi(123))

def masivs(n):
    m = []
    while n > 0:
        sk = n % 10
        n = (n - sk) // 10
        m.insert(0, sk)

    return m

print(masivs(1234))

def paraElemSkaits(masivs):
    skaits = 0
    for elem in masivs:
        if elem % 2 == 0:
            skaits += 1
    return skaits

print(paraElemSkaits([2, 4, 3, 5, 7]))

m = [1, 5, 8, 2 ,7, 3]
def augosi(m):
    for i in range(len(m) - 1):
        if m[i] > m[i + 1]:
            return False
    return True

if augosi(m):
    print(1)
else:
    print(0)

def lielakais(m):
    max = m[0]
    for elem in m:
        if elem > max:
            max = elem
    return max

while not augosi(m):
    for i in range(len(m) - 1):
        if m[i] > m[i + 1]:
            temp = m[i]
            m[i] = m[i + 1]
            m[i + 1] = temp