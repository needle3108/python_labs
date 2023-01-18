print('ZADANIE 1')

from copy import deepcopy
import random 
k = 10

t = [random.randrange(0,5*k) for i in range(k)]

l = deepcopy(t)

print('oryginal: ',t)
s = dict((i, 0) for i in range(k+1))

for j in range(100):
    random.shuffle(t)
    suma = sum( 1 for p in range(k) if t[p] == l[p])
    s[suma] += 1

print('liczba elementow ktora pozostala na swoim miejscu wzgledem oryginalu: ',s) 

print('\nZADANIE 3')

q = [random.randrange(0,20) for i in range(100)]

w = {}
h = {}

for i, x in enumerate(q):
    w.setdefault(x,[]).append(i)
print('PODPUNKT A \n',w)  

w.clear()

for i in q:
        w.setdefault(i,[]).append(q.index(i,w[i][-1]+1 if w[i] else 0))
            

print('PODPUNKT B \n',w)        

print('\nZADANIE 5')

v = dict((i, random.randrange(1,100)) for i in range(10))
b = dict((i, random.randrange(1,100)) for i in range(10))

v1 = {z: k for k, z in v.items()}
b1 = {z: k for k, z in b.items()}

print(v1)
print(b1)
