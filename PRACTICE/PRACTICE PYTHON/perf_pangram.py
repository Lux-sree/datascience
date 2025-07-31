def perf_pangram(word):
    if len(word)!=26:
        print("not pangram")
    else:
        char=ord('a')
        for i in range(0,26):
            letter=chr(char+i)
            if word.count(letter)!=1:
                print("not perfect pangram")
                break
        else:
            print("perfect pangram")
string=input("enter a string").lower()
string=''.join(filter(str.isalpha(),string))
perf_pangram(string)