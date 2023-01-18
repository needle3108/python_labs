print('ZADANIE 1'.center(80))

import sys

if len(sys.argv) == 1 :
    print('Prosze podac parametry startowe programu')
    sys.exit()

a=sys.argv[1:]  
print('Utworzony string: ',' '.join(a))

b=' '.join(a)

print('ZADANIE 2'.center(80))

low = [b[i] for i in range(len(b)) if b[i].islower()]
print(low)
uper = [b[i] for i in range(len(b)) if b[i].isupper()]
print(uper)
num = [b[i] for i in range(len(b)) if b[i].isnumeric()]
print(num)
other = [b[i] for i in range(len(b)) if not b[i].isalpha()]
print(other)

print('ZADANIE 3'.center(80))

once = [low[i] for i in range(len(low)) if low[i] not in low[:i]]
print(once)

counter = [(i,low.count(i)) for i in once]
print(counter)

print('ZADANIE 4'.center(80))

print(sorted(counter,key=lambda x: x[1],reverse=True))

print('ZADANIE 5'.center(80))

samogloski = ['a','e','i','o','u','y']

c_samogloski = 0
c_spolgloski = 0

for i in range(len(b)) :
    if b[i].lower() in samogloski[:]:
        c_samogloski += 1
    elif b[i].lower().isalpha :
        c_spolgloski += 1

print('Liczba samoglosek: ',c_samogloski, '\nLiczba spolglosek: ',c_spolgloski)

fun = [(int(i),c_samogloski*int(i) + c_spolgloski) for i in num]
print(fun)

print('ZADANIE 6'.center(80))

suma = sum(i for i,j in fun)

ave = suma/len(num)    
print('srednia: ',ave)

D = sum((i - ave)**2 for i,j in fun) 

print(D)    