def counts(s):
    dig=0
    letters=0
    spcl=0
    for i in s:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            dig+=1
        elif i in '!@#$%^&*()':
            spcl+=1
    return dig,letters,spcl

s=input("enter the string")
dig,letters,spcl=counts(s)
print(dig,letters,spcl)
