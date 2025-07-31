s=input("enter the string").split()
length=len(s[0])
largest=s[0]
lst=[]
for word in s:
    if len(word)>length:
        length=len(word)
for word in s:
    if length==len(word):
        lst.append(word)

print(lst)