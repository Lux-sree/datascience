#find the no of occurences of a particular character without using count function
str=input("enter the string")
n=input("enter the character whose occurrence count is to be found")
count=0
for i in str:
    if i==n:
        count+=1
print("occurence of",n,"is",count)


