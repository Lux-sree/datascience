# all factors of a  num,add all and if sum=num
def perfectno(num):
    s=0
    for i in range(1,num+1):
        if num%i==0:
            s+=i
    if s==num:
        return "perfectno"
    else:
        return "not perfectno"
no=int(input("enter a no"))
print(perfectno(no))