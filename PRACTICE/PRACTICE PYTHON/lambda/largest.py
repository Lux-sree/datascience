largest=lambda a,b,c: f"{a} is greater" if a>b and a>c else f"{b} is greater" if b>a and b>c else f"{c} is greater"
print(largest(3,4,5))