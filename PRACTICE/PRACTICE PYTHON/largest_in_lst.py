#def largest(lst):
#    g=int(lst[0])
#    for i in lst:
#        if int(i)>g:
#            g=int(i)
#    return g
#lst1=input("enter nos").split()
#print(largest(lst1))

#-----------------------------------

lst1=list(map(int,input("enter nos").split()))
print(max(lst1))