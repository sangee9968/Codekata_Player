#input
n,k=map(int,input().split(" "))
l=[]
for i in range(1,k+1):
	if n%i==0 and k%i==0:
		l.append(i)
print(l[-1])
