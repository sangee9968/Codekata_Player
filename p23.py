#input
n,k=map(int,input().split())
input()
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
s=[]
for i in range(len(l1)):
	l.append(l1[i])
	x=max(l)
	print(x)
	s.append(x)
print(*s)
