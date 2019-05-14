n,x=map(int,input().split())
l=list(map(int,input().split()))
a=1
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==x:
			a=0
if a==0:
	print("yes")
else:
  #result
	print("no")
		    
		    
