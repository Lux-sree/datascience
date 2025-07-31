def even_three(lst):

    even=[]
    three=[]
    for i in lst:
        if i%2==0:
            even.append(i)
    for i in lst:
        if i%3==0:
            three.append(i)
    return even,three

lst=[1,2,5,3,7,8,9,13,24,56]
even,three=even_three(lst)
print(even)
print(three)