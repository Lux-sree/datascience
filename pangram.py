#check if a given string is pangram or not
#ie all a-z elements are present ,no problem if letters repeate also
# You only need to ensure that each alphabet letter appears at least once
#str=input("enter the string").lower()
#word="abcdefghijklmnopqrstuvwxyz"
#flag=0
#
#for i in word:
#    if i in str:
#        flag=1
#    #elif i==" " or i.isdigit():
#    #    flag=1
#    else:
#        flag=0
#        break
#if flag==1:
#    print("is pangram")
#else:
#    print("is not pangram")
#
#_________________________________________________________________________
#The quick brown fox jumps over the lazy dog

str=input("enter a string")
ch=ord('a')  #97          #ord() to get the ascii value of the alphabet
for i in range(0,26):
    if chr(ch+i) not in str: #chr() to get the character of the ascii value
        print("not pangram")
        break
else:
    print("pangram")







