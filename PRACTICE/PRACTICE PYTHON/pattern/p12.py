#1 2 3 4
#2 3 4 5
#3 4 5 6
#4 5 6 7
s=1
for i in range(1,5):
    s=i
    for j in range(1,5):
        print(s,end=' ')
        s+=1
    print()