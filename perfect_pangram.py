str=input("enter string").lower()
ch=ord('a')

for i in range(0, 26):
    letter=chr(ch+i)
    if str.count(letter)!=1:
        print("not pangram")
        break
else:
    print("pangram")

