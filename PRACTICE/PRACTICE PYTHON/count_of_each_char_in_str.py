#str=input("enter a string")  #banana
#dic={}
#for ch in str:
#    dic[ch]=str.count(ch)
#print(dic)

#without using count function
str=input("enter a string")  #banana
dic={}
for i in str:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)


