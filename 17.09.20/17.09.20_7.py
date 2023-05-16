a=float(input('Ievadi 1. nogriežņa garumu'))
b=float(input('Ieavdi 2. nogriežņa garumu'))
c=float(input('Ievadi 3. nogriežņa garumu'))
if a+b>c and a+c>b and c+b>a:
    print('ir iespējams')
else:
    print('nav iespējams')
