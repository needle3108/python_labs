print("ZADANIE 1")

import sys
import random
from this import d

def funkcja1(f) :
    s = 'qwertyuiopasdfghjklzcvbnm'
    k = [str(random.randrange(0,10)) for i in range(25)]
    l =''.join(k)

    tr = str.maketrans(s,l)
    f=f.translate(tr)
    print('nasza funkcja:',f)

    wynik = []

    for i in range(10) :
        x = random.random()
        wynik.append((x, eval(f)))

    return wynik    

s = funkcja1(sys.argv[1]) 
print(s)

print("\nZADANIE 2")

def funkcja2(*a) :
    g = []
    for i in a[0] : 
        p = 0
        for j in range(len(a)) :
           if i not in a[j] :
               p = 1
        if p == 0 :
            g.append(i)
    return g    


l = funkcja2([1,2,3],(1,3,5),[3,2])
print(l)

