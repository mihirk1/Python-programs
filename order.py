s1=input()
s2=input()

x=len(s1)
y=len(s2)
i=0
j=0

while i<x and j<y:
    if s1[i]==s2[j]:
        j+=1
    i+=1

if j==y:
    print('Yes')
else:
    print('No')