def oddevens(upper,downno):
    lsteven=[]
    lstodd=[]
    count=0
    for i in range(downno,upper+1):
        if i%2==0:
            lsteven.append(i)
        else:
            lstodd.append(i)
    return lsteven,lstodd
up=int(input("Enter a up number: "))
down=int(input("Enter a low number: "))
l,s=oddevens(up,down)
print(l,"is the even list")
print(s,"is the odd list")

