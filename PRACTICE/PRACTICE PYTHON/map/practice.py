lst=['apple','orange','grapes','cherry']
lst1=list(map(lambda i:len(i),lst))
print(lst1)
lst2=list(map(lambda i:i.upper(),lst))
print(lst2)
lst3=list(map(lambda i:i.title(),lst))
print(lst3)
lst4=list(map(lambda i:list(i),lst))
print(lst4)