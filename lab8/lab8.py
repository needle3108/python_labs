print("ZADANIE 1")

def n_read(nazwa, n) :
    with open(nazwa) as file:
        line = file.readlines()
        print(line[:n])
        print(line[-n:])
        print(line[::n])
        print([el[n] for el in line if len(line) > n])

#n_read('data0.in', 2)

print("ZADANIE 2")

import glob
import numpy

dane = []

for file in glob.glob('data*in'):
    with open(file) as pl:
        values = [float(number) for number in pl]
        dane.append(values)

ave = [numpy.average(i) for i in zip(*dane)]
od_st = [numpy.std(i) for i in zip(*dane)]

iterator = [i for i in range(len(dane[0]))]

with open('data.out', 'w') as pl:
    for i in range(len(dane[0])):
        pl.write(f'{i} {ave[i]} {od_st[i]}\n')

print("ZADANIE 3")

def wykres(file):
    file.write("""import matplotlib.pyplot as plt
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
for file_name in glob.glob('data*in'): 
        y = numpy.loadtxt(file_name, unpack = True)
        plt.plot(range(len(y)), y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
    x, y, od = numpy.loadtxt('data.out', unpack = True)
    plt.errorbar(x, y, marker='*', yerr=od)
    #opis osi
    plt.xlabel('x')
    plt.ylabel('y')
#zapis do pliku, format określony przez rozszerzenie w nazwie
    plt.savefig('res.pdf')
    """)


with open('instrukcja.py', 'w') as pl:
    wykres(pl)

print("ZADANIE 4")

osoby = {}

for plik in glob.glob('20*txt'):
    with open(plik) as pl:
        for line in pl:
            year = plik[:4]
            name, place = line.split()
            osoby.setdefault(name,{}).setdefault(int(year), place)

with open('rank.out', 'w') as pl:
    for name in osoby.keys():
        pl.write(f'{name}\t')
        for rok in range(2000, 2020):
            if rok in osoby.get(name) :
                pl.write(f'{osoby.get(name).get(year)}\t {place}\n')    
        pl.write(f'\n')