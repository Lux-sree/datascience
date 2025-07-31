def prime(upper,lower):

    lstprime=[]
    for i in range(lower,upper+1):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            lstprime.append(i)
    return lstprime
up=int(input("enter the upper number"))
down=int(input("enter the down number"))
print(prime(up,down))