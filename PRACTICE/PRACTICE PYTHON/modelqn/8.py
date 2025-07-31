def duplicates(lst):
    lst1=[int(i) for i in lst]
    lst2=[]
    dic={}
    for i in lst1:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for k,v in dic.items():
        if v>1:
            lst2.append(k)
    return lst2

lst=input("enter the list").split()
print(duplicates(lst))