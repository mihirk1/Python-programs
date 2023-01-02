m=int(input())

l1=[]
for i in range(m):
    l1.append(input().split())


files=input().split()
#print(files)

q=int(input())
queries=[]
for j in range(q):
    queries.append(input())
   
fin=[]
for y in queries:
    fin.append(y.split(' '))
#print(fin)
#print(l1)

for item in fin:
    if item[0][-1]!='/':
        ak=item[0].split('/')
    else:
        ak='/'
    if item[1][-1]!='/':
        ak2=item[1].split('/')
    else:
        ak2='/'
    
    pos1=files.index(ak[-1])+1
    pos2=files.index(ak2[-1])+1
    l4=[]
    
    for hub in l1:
        if hub[0]==str(pos2):
            l4.append(hub[1])   
    
    cpos=[]
    xf=files.copy()
    ct=xf.count(item[2])
    for x in range(ct):
        cpos.append(str(xf.index(item[2])+1))
        xf[xf.index(item[2])]='ok'
    #print('l4',l4)
    #print('cpos',cpos)
    
    ans=[]
    for sm in l4:
        if sm in cpos:
            ans.append(False)
        else:
            ans.append(True)
    
    if False in ans:
        print('no')
    else:
        print('yes')
