def largest(str):
    lar=len(str[0])
    largest=str[0]
    lst=[]
    for i in str:
        if len(i)>lar:
            lar=len(i)
    for i in str:
        if len(i)==lar:
            lst.append(i)
    return lst



str=input("enter the string").split()
print(largest(str))