# Dotas trīs vārdnīcas a, b un c;
# Izveidot vārdnīcu d, kura veidojas triju vārdnīcu slēguma rezultātā - 
# īsceļu no vārdnīcas a atslēgu uz vārdnīcas c tulkojumu.
# Tātad, ja iekš a eksistē w:x, b - x:y, c - y:z, tad iekš d jābūt w:z.
# Vārdnīcu d sakārtot pēc atslēgas un izvadīt uz ekrāna.

a = {'c':'a', 'r':'t', 'y':'e', 'f':'b', 'w':'y', 'k':'j', 'm':'n'}
b = {'e':6, 'b': 7, 'x': 8, 'a':12, 'j':3, 'y':5, 'n':17, 'z':4, 'h':9}
c = {3:'L', 1:'K', 17:'s', 5:'a', 2:'g', 6:'b', 7:'a', 12:'i', 10:'v'}
d = {}

a2 = {}
d = {}

for key in a:
    if a[key] in b:
        a2[key] = b[a[key]]

for key in a2:
    if a2[key] in c:
        d[key] = c[a2[key]]

sorted_d = sorted(d, key=d.get, reverse=True)
print(sorted_d)