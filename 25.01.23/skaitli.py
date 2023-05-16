simti = {
    0:'',
    1:'simts',
    2:'divi simti',
    3:'trīs simti',
    4:'četri simti',
    5:'pieci simti',
    6:'seši simti',
    7:'septiņi simti',
    8:'astoņi simti',
    9:'deviņi simti'
}

desmiti = {
    0:'',
    1:'desmit',
    2:'divdesmit',
    3:'trīsdesmit',
    4:'četrdesmit',
    5:'piecdesmit',
    6:'sešdesmit',
    7:'septiņdesmit',
    8:'astoņdesmit',
    9:'deviņdesmit'
}

vieni = {
    0:'',
    1:'viens',
    2:'divi',
    3:'trīs',
    4:'četri',
    5:'pieci',
    6:'seši',
    7:'septiņi',
    8:'astoņi',
    9:'deviņi'
}

padsmiti = {
    0:'desmit',
    1:'vienpadsmit',
    2:'divpadsmit',
    3:'trīspadsmit',
    4:'četrpadsmit',
    5:'piecpadsmit',
    6:'sešpadsmit',
    7:'septiņpadsmit',
    8:'astoņpadsmit',
    9:'deviņpadsmit'
}

skaitlis = int(input("ievadi skaitli:"))

s = []
while skaitlis > 0:
    p = skaitlis % 10
    s.insert(0, p)
    skaitlis //= 10

while len(s) < 3:
    s.insert(0,0)
    
print(s)

if s[1] == 1:
    print(simti[s[0]], padsmiti[s[2]])
else:
    print(simti[s[0]], desmiti[s[1]], vieni[s[2]])