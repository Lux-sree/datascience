def lcmfind(a,b):
    if a>b:
        g=a
    else:
        g=b
    while True:
        if g%a==0 and g%b==0:
            lcm=g
            break
        g+=1
    return lcm
str1=int(input("enter 1st no"))
str2=int(input("enter 2nd no"))
print(lcmfind(str1,str2))