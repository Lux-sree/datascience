langs=['c','ccp','java','python']
p=list(filter(lambda n:'p' in n,langs))
print(p)
even=list(filter(lambda n:len(n)%2==0 ,langs))
print(even)
lst3=list(filter(lambda n:len(n)==4,langs))
print(lst3)
