print("Zadanie 1")
class Zakres:
    def __init__(self, st, en):
        self.start = st
        self.end = en

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        statement = True
        if self.start < self.end:
            for i in range(2, self.start):
                if (self.start % i) == 0:
                    statement = False
            if statement == True:
                return self.start
            else:
                pass            
        raise StopIteration

z = Zakres(3,10)

for i in z:
    print(f'{i}', end = ' ')
print("cos nie dziala ale nie wiem co :)\n")    

print("Zadanie 2")

class Pseudo:
    def __init__(self, en):
        self.m = 2**31 - 1
        self.a = 7**5
        self.c = 0
        self.x = 1
        self.start = 0
        self.end = en

    def __iter__(self):
        return self

    def __next__(self):
            self.x = (self.a * self.x + self.c) % self.m
            return self.x
 

pseudo = Pseudo(10**5)
x = [next(pseudo) / (2**31 - 1) for i in range(10**5)]
y = [next(pseudo) / (2**31 - 1) for i in range(10**5)]

for i in range(1, 11):
    ilosc = 0
    for elx, ely, in zip(x, y):
        if elx < (0.1 * i) and ely < (0.1 * i):
            ilosc += 1
    print("dla n = ", i, " miesci sie ", (ilosc / 10**5) * 100, "%")

import random

a = [random.random() for i in range(10**5)]
b = [random.random() for i in range(10**5)]

print("\n")
for i in range(1, 11):
    ilosc = 0
    for elx, ely, in zip(a, b):
        if elx < (0.1 * i) and ely < (0.1 * i):
            ilosc += 1
    print("dla n = ", i, " miesci sie ", (ilosc / 10**5) * 100, "%")

print("Zadanie 3")
import abc

class Calka(abc.ABC):
    def __init__(self, func, start, en):
        self.fun = func
        self.beg = start
        self.end = en

    @abc.abstractmethod
    def licz(self, n):
        return   

class Simpson(Calka):
    def licz(self, n):
        self.h = (self.end - self.beg) / (2 * n)

        self.start_value = self.fun(self.beg)
        self.end_value = self.fun(self.end)

        self.niepa = [self.fun(self.beg + (self.h*i)) for i in range(1, 2*n, 2)]
        self.pa = [self.fun(self.beg + (self.h*i)) for i in range(2, 2*n, 2)]
        self.np = 4 * sum(self.niepa)
        self.p = 2 * sum(self.pa)

        return (self.h/3) * (self.start_value + self.np + self.p + self.end_value)

A = Simpson(lambda x: x**2, 0 , 2)
print(A.licz(10000))

import scipy.integrate

print(scipy.integrate.quad(lambda x: x**2, 0 , 2))