def happy(num):
    s=0
    while num>0:
        rem=num%10
        s+=rem**2
        num=num//10
    return s
num=int(input("enter a number"))
lst=[]
while num!=1 and num not in lst:
     lst.append(num)
     num=happy(num)
if num==1:
    print("happy no")
else:
    print("not happy no")


