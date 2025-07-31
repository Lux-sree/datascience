def fibanocci(n):
    a=0
    b=1
    for _ in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
num=int(input("enter no1"))
fibanocci(num)