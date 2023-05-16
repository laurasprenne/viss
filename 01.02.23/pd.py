vieni = {
    0:'',
    1:'pirmais',
    2:'otrais',
    3:'trešais',
    4:'ceturtais',
    5:'piektais',
    6:'sestais',
    7:'septītais',
    8:'astotais',
    9:'devītais'
}

desmiti = {
    0:'',
    1:'',
    2:'divdesmit',
    3:'trīsdesmit'
}

padsmiti = {
    0:'desmitais',
    1:'vienpadsmitais',
    2:'divpadsmitais',
    3:'trīspadsmitais',
    4:'četrpadsmitais',
    5:'piecpadsmitais',
    6:'sešpadsmitais',
    7:'septiņpadsmitais',
    8:'astoņpadsmitais',
    9:'deviņpadsmitais'
}

menesi = {
    '01':'janvāris',
    '02':'februāris',
    '03':'marts',
    '04':'aprīlis',
    '05':'maijs',
    '06':'jūnijs',
    '07':'jūlijs',
    '08':'augusts',
    '09':'septembris',
    '10':'oktobris',
    '11':'novembris',
    '12':'decembris'
}

datums = input("ievadi datumu:")

date = datums.split(".")

d = int(date[0])
m = date[1]
day = []

while d > 0:
    p = d % 10
    day.insert(0, p)
    d //= 10

while len(day) < 3:
    day.insert(0,0)

if day[0] == 1:
    print(padsmiti[day[1]], menesi[m[0]])
else:
    print(desmiti[day[0]], vieni[day[1]], menesi[m[0]])