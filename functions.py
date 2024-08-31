def add(a,b):
    return a+b

def futurefunction(a,b):
    pass
a = 10
b = 100

print(futurefunction(10,11))
print(add(a,b))

def futurefunction(a,b):
    return a+b
#ouput
# None
# 110


#function arguments
#default
#keyword
#variable length
#requred arguments
def average(a=9,b=2):
    print("the average is ",(a+b)/2 )
    
average(34,12)
average(3)
average(b=9)

# #output
# the average is  23.0
# the average is  2.5
# the average is  9.0