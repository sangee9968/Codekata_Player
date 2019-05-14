n=int(input())
l=[]
for i in range(1,n+1):
    q=n//i
    if q%2!=0 and n%i==0:
    	l.append(i)
#result      
print(l[0])    	
    	
    
	
