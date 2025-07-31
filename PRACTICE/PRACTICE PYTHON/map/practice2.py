lst=[1,2,3,4,5,6]
lst1=list(map(lambda n:n if n%2==0 else n*n,lst))
print(lst1)
lst2=list(map(lambda n:n+1 if n>3 else n,lst))
print(lst2)
lst3=list(map(lambda n:n+2 if n<5 else n,lst))
print(lst3)
lst4=list(map(lambda n:n**3 if n<3 else n**2,lst))
print(lst4)