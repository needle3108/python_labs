k = [1, 2.3, '3', (4,7), [2,3,4],]

c=k
c[1] = [7,8,9]
print(c, k)
print(id(c), id(k))

c=k[:]
c[1]='7,8,9'
print(c, k)
print(id(c), id(k))

c[-1][1]='7,8,9'
print(c, k)

c=k.copy()
c[1]='7,8,9'
print(c, k)
print(id(c), id(k))

c[-1][1]='7,8,9'
print(c, k)

