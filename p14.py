st=""
n=int(input())
s=input()
s1=s[::-1]
l=list(s1)
l1=['a','e','i','o','u']
for i in l:
	for j in l1:
		if j in i:
			l.remove(j)
for i in l:
	st=st+str(i)+""
#result  
print(st.strip())	
