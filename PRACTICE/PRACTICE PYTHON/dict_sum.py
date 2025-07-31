dic1={'a':1,'b':2,'c':3}
dic2={'b':5,'c':6,'d':7}

for k,v in dic1.items():
    if k in dic2.keys():
        dic2.update({k:v+dic2[k]})
    else:
        dic2.update({k:v})
print(dic2)
