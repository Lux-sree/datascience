def even(lst):
    lst1=[int(i) for i in lst]
    s=0
    for i in lst1:
        if i%2==0:
            s+=i
    return s

lst=input("enter the list").split()
print(even(lst))