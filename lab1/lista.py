k=[]
print(type(k))
k=[2]
print(type(k))
k=[2,]
print(type(k))

k=[1,2.3,'3',(4,7),[2,3,4],]
print(len(k))

print(k[0], k[len(k)-1], k[-1])

k[-2] = 'byla krotka ale znikla'
print(k)

k=[12,67,3,5,0,-12,7,3,3,2,1]
print(k[2:8:2])
print(k[::-1])