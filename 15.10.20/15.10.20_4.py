x=int(input('Ievadi x vērtību'))
y=int(input('Ievadi y vērtību'))
if x>0 and y>0:
    print('punkts atrodas 1. kvadrantā')
elif x<0 and y>0:
    print('punkts atrodas 2. kvadrantā')
elif x<0 and y<0:
    print('punkts atrodas 3. kvadrantā')
elif x>0 and y<0:
    print('punkts atrodas 4. kvadrantā')
else:
    print('punkts atrodas uz koordinātu taisnes')
if 2*y==6*x-7:
    print('punkts pieder taisnei 2y=6x-7')
else:
    print('punkts nepieder taisnei 2y=6x-7')