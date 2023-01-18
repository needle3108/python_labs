print('zadanie 1')

k=[17, 32, -88, 2, 2, 45, 99, 103, -234,]
for i in range(len(k)-1,-1,-1):
    if k[i] == 2 :
        del k[i]
print(k)

print('zadanie 2')

k=[17, 32, -88, 2, 2, 45, 99, 103, -234,]
d=len(k)-1
while d>=0 :
    if k[d] == 2:
        del k[d]
    d-=1
print(k)    

print('zadanie 3')

k=[17, 32, -88, 2, 2, 45, 99, 103, -234,]

for i in range(1,len(k),2) :
    print(k[i], end=', ')

print('\nzadanie 4')    

print(k[1::2])

print('zadanie 5')

for i in range(len(k)-1,-1,-2) :
    print(k[i], end=', ')

print('\nzadanie 6')        

print(k[len(k)-1::-2])

print('zadanie 7')

p=[(i, k[i]) for i in range(len(k))]

print(p)

print('zadanie 8')

p.sort(key=lambda x:x[1])
print(p)

print('zadanie 9')

d=[(i, k[i]) for i in range(len(k)) if k[i]%2==0]
print(d)

print('zadanie 10')

l=[(i, k[i]) if k[i]>i else (k[i], i) for i in range(len(k))]
print(l)

print('zadanie 11')

h=[[]]

N=4
n=2
