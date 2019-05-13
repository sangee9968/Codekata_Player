s=""
n,k=map(int,input().split())
l=list(map(int,input().split()))
l= (l[len(l) -k:len(l)] + l[0:len(l) - k]) 
for i in l:
    s=s+str(i)+" "
print(s.strip())
