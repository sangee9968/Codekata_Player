n=int(input())
l3=[]
s=""
l4=[]
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l1:
	for j in l2:
		if i==j:
			l3.append(i)
l4=list(set(l3))
for i in l4:
	s=s+str(i)+" "
#result  
print(s.strip())
