#if all alphabets present in a string and any other char can also occur
def pangram(word):
    char=ord('a') #97
    for i in range(0,26):
        if chr(char+i) not in word:
            print("not pangram")
            break
    else:
        print("pangram")

string=input("enter a string")
pangram(string)