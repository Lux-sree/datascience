def missing(lst):
    lst1=[int(i) for i in lst]
    mini=min(lst1)
    maxi=max(lst1)
    for i in range(mini,maxi+1):
        if i not in lst1:
            return i

lst=input("enter the list").split()
print(missing(lst))