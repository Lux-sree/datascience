oc=[1,2,3]
cl=[]
for i in oc:
    for j in oc:
        for k in oc:
            if i!=j and j!=k and k!=i:
                cl.append([i,j,k])
print(cl)