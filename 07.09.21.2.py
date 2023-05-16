a=[]
sum = 0
x = int(input('Ievadi skaitli'))
while x != 0:
    sum += x
    a.append(x)
    x = int(input('Ievadi skaitli'))

print(sum)
print(a)

#3
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])
        
#4        
for i in range(len(a)-1, -1, -1):
    print(a[i])
    
#5
liel = a[0]
if a[i] % 2 == 0 and a[i] > liel:
    a[i] = liel
    
print(liel)



