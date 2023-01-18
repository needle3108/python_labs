print('ZADANIE 1')

import time
import sys
import random
import math

from numpy import average

powt = 1000
N = 10000

def forStatement():
    wynik = []
    for i in range(N):
        wynik.append(i)
    return wynik

def listComprehension():
    return [i for i in range(N)]

def mapFunction():
    return list(map(lambda x: x, range(N)))

def generatorExpression():
    return list((i for i in range(N)))

def tester(fun):
    start = time.time_ns()
    for i in range(powt):
        fun()
    return time.time_ns() - start    

print(sys.version)
test = (forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20),'=>',tester(testFunction))

print('\nZADANIE 2')

l1 = [random.randrange(0,20) for i in range(100)]
l2 = [random.randrange(0,20) for i in range(100)]

result = list(filter(lambda x: 3 < (x[0] + x[1]) < 15,zip(l1,l2)))
print(result)

print('\nZADANIE 3')
n = 100

x1 = [i for i in range(n)]
y1 = [3*i + 7 for i in x1]

def f1(x, y):
    result = []

    ave_x = sum(x)/n
    ave_y = sum(y)/n
    D = sum(map(lambda val: (val - ave_x)**2,x))
    a = sum(map(lambda valx, valy: valy*(valx - ave_x),x,y))/D
    b = ave_y - (a * ave_x)

    delta_y = math.sqrt(sum(map(lambda valx, valy: (valy - (a * valx + b)),x,y))/(n-2))
    delta_a = delta_y/math.sqrt(D)
    delta_b = delta_y*math.sqrt((1/n) + (ave_x**2/D))

    result.append(a)
    result.append(b)
    result.append(delta_a)
    result.append(delta_b)
    
    return result

wspolczynniki = f1(x1,y1)    
print(wspolczynniki)

print('\nZADANIE 4')

values = [1,2,3,10,]

def myreduce(f, s):
    a = s[0]
    for i in range(1,len(s)):
        a = f(a,s[i])
    return a

res = myreduce(lambda x,y: x + y, values)
print('Dodawanie:',res)

res = myreduce(lambda x,y: x * y, values)
print('Mnozenie:',res)

print('\nZADANIE 5')
dimension = 4

macierz = [[(i*j)**2 for j in range(dimension)] for i in range(dimension)]

print('max w kazdym wierszu:',list(map(max,macierz)))
print('max w kazdej kolumnie:',list(map(max,zip(*macierz))))