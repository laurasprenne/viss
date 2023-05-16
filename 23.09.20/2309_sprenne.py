a=float(input("Ievadi punktu skaitu!"))
max=float(input('Ievadi max punktus'))
p=a/max*100
if p>=1 and p<11:
    print('1')
elif p>=11 and p<21:
    print('2')
elif p>=21 and p<35:
    print('3')
elif p>=35 and p<50:
    print('4')
elif p>=50 and p<60:
    print('5')
elif p>=60 and p<70:
    print('6')
elif p>=70 and p<80:
    print('7')
elif p>=80 and p<88:
    print('8')
elif p>=88 and p<96:
    print('9')
else:
    print('10')
