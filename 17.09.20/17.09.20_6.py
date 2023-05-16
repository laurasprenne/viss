sk1=float(input('Ievadi vienu skaitli!'))
sk2=float(input('Ievadi otru skaitli!'))
sk3=float(input('Ievadi trešo skaitli!'))
if sk1>sk2 and sk1>sk3:
    print('lielākais skaitlis ir', sk1)
elif sk2>sk1 and sk2>sk3:
    print('lielākais skaitlis ir',sk2)
else:
    print('lielākais skaitlis ir',sk3)
    