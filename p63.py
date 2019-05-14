n=int(input())
l3=[]
s=""
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l1:
	if i in l2 and i not in l3:
		l3.append(i)
for i in l3:
	s=s+str(i)+" "
#result	
print(s.strip())	
