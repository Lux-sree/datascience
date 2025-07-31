def pallindrome(num):
    number=num
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if rev==number:
        print("pallindrome")
    else:
        print("not pallindrome")
num=int(input("enter number:"))
pallindrome(num)