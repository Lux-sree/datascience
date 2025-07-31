def gcdfind(a,b):
    if a>b:
        l=b
    else:
        l=a
    while l!=0:
        if a%l==0 and b%l==0:
            gcd=l
            break
        l-=1
    return gcd
no1=int(input("enter no1"))
no2=int(input("enter no2"))
print(gcdfind(no1,no2))