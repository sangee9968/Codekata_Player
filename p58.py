s1=input()
s2=input()
c=0
l=list(s1.split(" "))
for i in range(0,len(l)):
  if l[i]==s2:
    c=c+1
#result    
print(c)
