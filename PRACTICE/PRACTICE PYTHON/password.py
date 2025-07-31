def password(string):
    digit=False
    low=False
    spcl=False
    up=False
    if len(string)>=8:
        for i in string:
            if i.isdigit():
                digit=True
            elif i.isupper():
                up=True
            elif i.islower():
                low=True
            elif i in '!@#$%^&*()':
                spcl=True
        if digit==True and low==True and up==True and spcl==True:
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")

string=input("enter a string")
password(string)


