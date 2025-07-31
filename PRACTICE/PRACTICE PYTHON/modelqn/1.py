def counts(str,no):
    count_original=s.count('a')
    full_len_times=no//len(str)
    rem=no%len(str)
    rem_count=s[:rem].count('a')
    ans_count=(count_original*full_len_times)+rem_count
    return ans_count


s=input("enter the string")
n=int(input("enter the number of chars needed"))
print(counts(s,n))