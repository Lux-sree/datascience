#find the index of a charracter wherever it appears in the string
str=input("enter a string")
c=input("enter a character")
for i in range(0,len(str)):
    if str[i]==c:
        print(i)                         #cant use index() here,as it gives only index of 1st appearance of the char