s1='luminar technolab'
#forward indexing
print(s1[1])    #u
print(s1[11])   #h
print(s1[16])   #b
#backward indexing
print(s1[-4])   #o
print(s1[-11])  #r
print(s1[-1])   #b

#slice forward
print(s1[0:3])  #lum
print(s1[8:12]) #tech
print(s1[14:])  #lab
print(s1[2:5])  #min
#slice backwards
print(s1[-17:-14])  #lum
print(s1[-9:-5])    #tech
print(s1[-3:])      #lab
print(s1[-15:-12])  #min
s2='luminar'
print(s2[4:1:-1])   #nim
print(s2[::-1])   #ranimul-backward
print(s2[6::-1])    #ranimul-forward

s2="PYTHon is"
print(s2.upper())
print(s2.lower())
print(s2.swapcase())
print(s2.title())
print(s2.capitalize())
print(len(s2))
s3="python123"
print(s3.isupper()) #also atleast one char should be there
print(s3.islower())  #also atleast 1 char should be there
print(s3.isdigit())
print(s3.isalpha())
print(s3.isalnum())
s4="@@@@python#@@@@"
print(s4.strip('@#'))
print(s4.lstrip('@#'))
print(s4.rstrip('@#'))
print(s4.replace('p','r'))

