def longest(string):
    maxi=len(string[0])
    for i in string:
        if len(i)>maxi:
            maxi=len(i)
    for i in string:
        if len(i)==maxi:
            print(i)



string=input("enter string").split()
longest(string)