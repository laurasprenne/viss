import random
dators=random.randint(1,100)
skaits=0
lietotajs=0
while lietotajs!=dators:
    lietotajs=int(input('Ievadi skaitli'))
    skaits=skaits+1
    if lietotajs>dators:
        print('datora skaitlis ir mazāks')
    elif lietotajs<dators:
        print('datora skaitlis ir lielāks')
print('Uzminēji ar' , skaits,'. reizi')
