l,r=map(int,input().split())
c=0
for i in range(l,r):
    for j in range(2,i+1):
        if i%j==0:
           break
        else:
            c=c+1
#result            
print(c)       
