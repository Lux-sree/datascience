str=input("Enter a string: ")
n=input("Enter a char for index: ")
for i in range (len(str)):
    if str[i]==n:
        print(i)
print(str.isupper())
print(str.islower())