import copy

k = [1, 2.3, '3', (4,7), [2,3,4],]

c=copy.copy(k)

c[1] = '7,8,9'

print(c, k)
print(id(c), id(k))

c=copy.deepcopy(k)
c[1] = '7,8,9'
print(c, k)
print(id(c), id(k))

c[-1][1] = '7,8,9'
print(c, k)

print('\nZliczanie')

k=[8,0,17,1,10,13,19,13,10,3,]

print(k.count(13))
print(k.count(-13))

#print(k.index(13))
#print(k.index(-13))

print(13 in k)
print(-13 not in k)

if 13 in k:
    print(k.index(13))

if -13 not in k:
    pass    

print('\ninsert ')

k.insert(4,-13)
print(k)

k.insert(-23,4)
k.insert(23,4)
print(k)

k[1:4]=[7,8,9,10,]
print(k)

k[1:4]=[[7,8],]
print(k)

print('\nremove')

k.remove(1)
print(k)

del k[3]
print(k)

del k[-3:]
print(k)

k.clear()
print(k)

print('\nRozbudowywanie listy')

k=[1]*10
k[3]+=1

print(k)

k=[[]]*10
k[3].append(1)

print(k)

print('\nlista skladana')

k=[[] for i in range (10)]
k[3].append(1)

print(k)

k[3].append([1,2,3])
print(k)
k[3].extend([1,2,3])
print(k)

k[3].append('1,2,3')
print(k)
k[3].extend('1,2,3')
print(k)

print('\nrange')

k=[]
for i in range(10):
    k.append(i)

print(k)    

k=list(range(10))
print(k)

k=list(range(3,10))
print(k)

k=list(range(3,10,2))
k=[8,0,17,1,10,13,19,13,10,3,]

print('\npetla')

for i in k:
    i*=2
    print(i, end=', ')
print('\n',k)    

for i in range(len(k)):
    k[i]*=2

print(k)     

for i,v in enumerate(k):
    k[i] = 1 if v>0 else -1

print(k)    

for i in k:
    if i%2:
        break
else:
    print('kiedy?')    

k=[8,0,17,1,10,13,19,13,10,3,]

np=[i for i in k if i%2]
print(np)
np=[1 if i>0 else -1 for i in k]

print(np)

k=[(k[i], k[-i-1]) for i in range(len(k)//2)]
print(k)

print('\npetla zagniezdzona')

N=3
k=[]
for i in range(N):
    tmp=[]
    for j in range(N):
        tmp.append((i,j))
    k.append(tmp)
print(k)        

k=[[(i,j) for j in range(N)] for i in range(N)]

print('\nsortowanie')

k=[(89, 34), (92, 31), (96, 0), (48, 30), (38, 10),]
c=k[:]
c.sort()
print(c)

c=k[:]
c.sort(key=lambda x: x[1])
print(c)

c=k[:]
c.sort(reverse=True)
print(c)

c=k[:]
for i,j in sorted(c):
    print(i,j)
print(c)    
