def armstrong(up,down):
    lst=[]
    for i in range(down,up+1):
        s=str(i)
        p=len(s)
        su=0
        temp=i
        while i>0:
            rem=i%10
            su=su+rem**p
            i=i//10
        if temp==su:
            lst.append(temp)
    return lst
up=int(input("enter the up number of chars needed"))
down=int(input("enter the down number of chars needed"))
print(armstrong(up,down))