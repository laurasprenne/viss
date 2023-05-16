dar=input('Ievadi kādu darbūbu veiksi? (+,-,/,*)')
if dar=='/' or dar=='-':
    print('Atceries, ka ir svarīgi, kuru skaitli ievadi pirmo')
a=float(input('Ievadi pirmo skaitli!'))
b=float(input('Ievadi otro skaitli!'))
if dar=='/' and b==0:
    print('Ar 0 dalīt nedrīkst!')
if dar!='/' and dar!='+' and dar!='-' and dar!='*':
    print('Ievadīji nenolasāmu darbību')
if dar=='+':
    print(a, dar, b, '=', a+b)
elif dar=='-':
    print(a, dar, b, '=', a-b)
elif dar=='/':
    print(a, dar, b, '=', a/b)
elif dar=='*':
    print(a, dar, b, '=', a*b)