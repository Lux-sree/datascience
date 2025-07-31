def pal(str):
    stri=str[::-1]
    if str==stri:
        print("palindrome")
    else:
        print("not palindrome")

string = input("enter a string")
pal(string)