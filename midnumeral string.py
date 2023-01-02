import re
import sys
m=input()
r1=[]
wait=[]

count=0

for i in m:
    if re.findall('[a-zA-Z]',i):
        r1.append(i)
    elif len(wait)==0:
        wait.append(i)
    else:
        
        if wait[-1]=='(':
            wait.append(i)
        
        elif i=='(':
            wait.append(i)

        elif i==')':
                wait.append(')')
                wait.reverse()
                pos1=wait.index('(')
                pos2=wait.index(')')
                
                wait2=wait[pos2:pos1+1]
                wait2.remove('(')
                wait2.remove(')')
                
                wait.remove('(')
                wait.remove(')')
                wait.reverse()
                for j in wait2:
                    r1.append(j)
                    wait.remove(j)
                    

                    
                
        elif int(wait[-1])<int(i):
            wait.append(i)
        elif int(wait[-1])>int(i):
            r1.append(wait[-1])
            wait.remove(wait[-1])
            wait.append(i)
    
    count+=1
    if count==len(m):
        wait.reverse()
        for x in wait:
            r1.append(x)

r=''.join(r1)
print(r)