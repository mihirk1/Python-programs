s=input()
l1=[]
for i in s:
    l1.append(i)
s1=set(l1)
d1=sorted(list(s1))

combo=[]
for i in d1:
    for j in d1:
        if i!=j:
            combo.append([i,j])
            
l3=[]
for i in combo:
    l2=l1.copy()
    for j in i:
        ct=l2.count(j)
        for x in range(ct):
            l2.remove(j)
    l3.append(''.join(l2))

s2=set(l3)
l4=list(s2)
l4.sort()
lt=[]
for i in l4:
    lt.append(len(i))

pos=lt.index(max(lt))
print(l4[pos])