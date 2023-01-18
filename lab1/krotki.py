k=()
print(type(k))
k=(2)
print(type(k))
k=(2,)
print(type(k))

k=(1,2.3,'3',(4,7),[2,3,4],)
print(len(k))

k[-1][1] = 'masno'
print(k)