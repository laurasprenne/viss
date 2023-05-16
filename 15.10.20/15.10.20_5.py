x=int(input('Cik skaitļus izvadīsi?'))
dc=0
for i in range(x):
    a=int(input('Ievadi skaitli'))
    if a>=10 and a<=99:
        dc=dc+1
    elif a<=-10 and a>=-99:
        dc=dc+1
        
print('lietotājs ievadīja', dc, 'divcipara skaitļus')
    
