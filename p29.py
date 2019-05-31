#input
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
	for j in range(1,i+1):
		if j**2==i:
			c+=1
print(c)
