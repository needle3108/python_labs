print("ZADANIE 1")

print("TUTAJ POWINIEN BYC TROJKAT PASCALA ALE GO NIE MA :(")

print("\nZADANIE 2")

def gen_2(seq):
    zero = 0
    for i in seq:
        if i == 0:
            zero += 1
        else:
            yield zero
            zero = 0           

import random

N = 10000

seq = [random.randint(0,1) for _ in range(N)]

zero = [i for i in gen_2(seq)]

ave = sum(zero)/len(zero)

print(f"srednia {ave}")

print("\nZADANIE 3")

def gen_3_1():
    a=0
    b=1
    while True:
        yield a
        a, b = b, a + b

def gen_3_2_1(s):
    for i in s:
        if i%2:
            yield i

def gen_3_2_2(s):
    for i in s:
        if not i%2:
            yield i

def gen_3_3(s, k):
    for i in s:
        if i < k:
            yield i
        else:
            return    

print(sum(gen_3_2_1(gen_3_3(gen_3_1(),100))))
print(sum(gen_3_2_2(gen_3_3(gen_3_1(),100))))

print("\nZADANIE 4")

def gen_4(*para):
    if len(para) == 1 and para[0] > 0:
        start, end, step = 0.0, float(para[0]), 1   
    elif len(para) == 2 and para[0] < para[1]:
        start, end, step = float(para[0]), float(para[1]), 1
    elif len(para) == 3 and para[0] < para[1] and para[2] > 0:
        start, end, step = float(para[0]), float(para[1]), float(para[2])
    elif len(para) == 3 and para[0] > para[1] and para[2] < 0:
        start, end, step = float(para[0]), float(para[1]), float(para[2])
    else:
        return    
    
    if start < end:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step

print(list(gen_4(7)))
print(list(gen_4(-7)))
print(list(gen_4(2,7)))
print(list(gen_4(7,2)))
print(list(gen_4(2,7,2)))
print(list(gen_4(2,7,-2)))
print(list(gen_4(7,2,2)))
print(list(gen_4(7,2,-2)))

print("\nZADANIE 5")

import math

def gen_5(a):
    u = 0
    x = 1
    i = 1
    
    while x != 1.5:
        u += a/x
        x = 1 + i*a
        yield x, u, math.log(x)
        i += 1


a = 0.05
print(list(gen_5(a)))
