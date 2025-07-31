def leap(year):
    leaplst=[]
    for i in year:
        if int(i)%4==0 and int(i)%100!=0 or int(i)%400==0:
            leaplst.append(i)
        else:
            pass
    return leaplst
years=input("enter years:").split()
print(leap(years))