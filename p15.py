s=input()
l=list(s)
dict = {i:l.count(i) for i in l}
maximum = max(dict, key=dict.get)  
#result
print(maximum)
