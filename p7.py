s=input()
l=list(s)
for i in range(0,len(l)):
    if i%2==0:
        l[i],l[i+1]=l[i+1],l[i]
#result        
print(''.join(l))        
