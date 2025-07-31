def sec_large(lst):
    lst1=[int(i) for i in lst]
    lst1.sort()
    print(lst1[-2])

lst=input("enter the lst").split()
sec_large(lst)
