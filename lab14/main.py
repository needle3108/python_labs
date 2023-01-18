import sys
sys.path.append('build/lib.linux-x86_64-3.9')
import mod
import random
import time
import copy

print("Zadanie 1")

def sorta(l, n):
    for x in range(1,n):
        selected = l[x]
        y = x-1
        while y>= 0 and selected < l[y]:
            l[y+1] = l[y]
            y -= 1
        l[y+1] = selected        


print(mod.met(1,2))
print(mod.met(1,2,5))
print(mod.met(1,2,5,[2,3,4]))

print("\nZadanie 2")

for x in range(1,5):
    lista = [random.randint(0, 10**x) for _ in range(10**x)]
    lista2 = copy.deepcopy(lista)

    print("Rozmiar: ",10**x)
    
    t0=time.time()
    sorta(lista, len(lista))

    print("Sortowanie w Pythonie:",time.time() - t0)

    t0=time.time()
    lista_sort_c = mod.sort(lista2)

    print("Sortowanie w C:",time.time() - t0,"\n")



