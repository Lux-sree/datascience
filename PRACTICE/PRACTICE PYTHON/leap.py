def leap(num):
    if num%4==0 and num%400==0:
        return "leap year"
    elif num%4==0 and num%100!=0:
        return "leap year"
    else:
        return "not leap year"
number=int(input("enter number:"))
print(leap(number))
