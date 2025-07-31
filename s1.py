str=input('Enter a string')
uc=0
lc=0
dc=0
ws=0
for i in str:
    if i.isupper():
        uc+=1
    elif i.islower() and i.isdigit()==False:
        lc+=1
    elif i.isdigit():
        dc+=1
    elif i==' ':
        ws+=1
print(uc)
print(lc)
print(dc)
print(ws)
