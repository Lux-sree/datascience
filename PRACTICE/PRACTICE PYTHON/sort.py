#def sort(lst):
#    for i in range(0,len(lst)):
#        for j in range(0,len(lst)-i-1):
#            if lst[j]>lst[j+1]:
#                lst[j],lst[j+1] = lst[j+1],lst[j]
def sort(lst):
    lst1=[int(i) for i in lst]
    lst2=[]
    while lst1!=[]:
        smallest = min(lst1)
        lst1.remove(smallest)
        lst2.append(smallest)
    return lst2

lst=input("enter numbers separated by spaces").split()
print(sort(lst))