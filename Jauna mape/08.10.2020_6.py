import random
dators=random.randint(1,10)
lie=int(input('ievadi skaitli no 1-10'))
skaits=1
while dators!=lie:
    dators=random.randint(1,10)
    skaits=skaits+1
if dators==lie:
    print('dators minēja' , skaits, 'reizes')
    