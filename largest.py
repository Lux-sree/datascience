#find the largest word in a given sentence
#lst=input("enter the sentence").split()
#for i in range (len(lst)):
#    lar=len(lst[0])
#    largest=lst[0]

#    if len(lst[i])>lar:
#        largest=lst[i]
#print(largest)

#________________________________
#if more than one same length words come
lst=input("enter the sentence").split()
for i in range (len(lst)):
    lar=len(lst[0])
    largest=lst[0]

    if len(lst[i])>lar:
        largest=lst[i]
    length=len(largest)
#print("word",largest)
for i in range(len(lst)):
    if len(lst[i])==length:
        print(lst[i])


