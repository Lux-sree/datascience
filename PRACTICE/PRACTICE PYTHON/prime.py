def prime(num):
    count=0
    if num==1:
        print("not prime")
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not prime")
number=int(input("Enter a number: "))
prime(number)