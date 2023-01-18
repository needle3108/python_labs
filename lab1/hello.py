#!/usr/bin/env python3
import keyword
#print(keyword.kwlist)

import builtins
#print(dir(builtins))

import math
#print(dir(math))
#help(math.modf)

print(type(''))
print(type(""))

a=7
print(type(a))

a=1.5
print(type(a))

a=1,1
print(type(a))

a,*b=1,'2',3.,4,5
print(type(a), type(b))

print(1/2, 1//2)
print(1./2, 1.//2)

print(2**3, pow(2,3),  math.pow(2,3))
print(pow(2,3,4), pow(2,3,5))

print(math.ceil(1/3), math.floor(1/3), round(1/3), round(1/3,3))

print(math.modf(1/3), math.modf(2.5))

print(min(2,11,34,90,-34))
print(max(17,0,34,88,22))

a=-1.7
print(abs(a), math.fabs(a))

a=-1
print(abs(a), math.fabs(a))

