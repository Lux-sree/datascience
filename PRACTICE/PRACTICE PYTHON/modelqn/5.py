def anagram(s1,s2):
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    print(s1,s2)
    if s1==s2:
        print("anagram")
    else:
        print("not anagram")

s1=input("enter the string")
s2=input("enter the string")
anagram(s1,s2)