d = "saadva"
type(d)

213.31+3216.2 

n = True
type(n)

m = False
type(m)

True * False
True + False
True / False #error in core py but in numpy we get infinite for 1/0

d ="fsdFW" # or single cortes


u = 5+8i #error
v = 5+8j#convention for iota - imagiary no.  in py

type(v)

v.imag
v.real
type(v.real)

print("sdbgdf")


s = "WAFASVD"
type(s)

s[0]#forward indexing
s[-1]#backward indexing 

s[0:3]#to excess mulipl,e indices till n-1

s[0:4]
len(s)
s[0:7:2]#initial : start:  jump

s[0::2]#if last  not given  wo aapne aap end index tk chalega

s[::-1] #reverse -- just giving the jump -1


#understand the previous
s[2:7:-1]#blank
s[7:0]#blank bcz by default jump =1

s[7:0:-1]# will not reverse bcx last index se ek pehle tk khatm ho jayega

s[::]#all data
s[::1]#all data


s[::90]#upper index doesn't matter in slicing ...byy defaulkt last wala le lega
s[:90:]


s[90]#out of range

c=200#enko slice nhi kr shakte

s1 = "this is my string class"
len(s1)#white space too
s1.find("is")#first occurance 
s1.find("s")

s1.find("i")
s1.count("s")#no. of substrings 

s2 = s1.upper()
s2
s3 = s2.lower()
s3


s1.capitalize()#only first leeter of whole string
s1.title() # first letter capital of whole word in the string




