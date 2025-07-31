#heart earth
def anagram(w1,w2):
    lst1=list(w1)
    lst2=list(w2)
    lst1.sort()
    lst2.sort()
    if lst1==lst2:
        print("anagram")
    else:
        print("not anagram")
word1=input("enter a word")
word2=input("enter a word")
anagram(word1,word2)