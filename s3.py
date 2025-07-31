#find no of chars in a string,not including space
str=input("enter the string")
count=0
for i in str:
    if i!=' ':
        count+=1
print("no of chars in string is :",count)