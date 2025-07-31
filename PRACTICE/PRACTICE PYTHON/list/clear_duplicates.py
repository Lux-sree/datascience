def duplic(lst):
    lst1=[]
    for i in lst:
        if i not in lst1:
            lst1.append(i)
        else:
            pass
    return lst1
lst=[1,2,2,2,3,4,4,5]