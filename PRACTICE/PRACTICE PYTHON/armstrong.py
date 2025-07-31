#ARMSTRONG--153--->1^3+5^3+3^3=153 then armstrong
def armstrong(num):
    p=len(str(num))
    s=0
    no=num
    while num>0:
        rem=num%10
        s=s+rem**p
        num=num//10
    if s==no:
        print("armstrong")
    else:
        print("not armstrong")


num=int(input("enter the number"))
armstrong(num)