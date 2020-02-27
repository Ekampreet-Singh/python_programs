def plus(*value):
    sum=0
    for number in value:
        sum+=number
    print("sum =",sum)

plus(21,    25,26,2365)        
 
 # here *value is variable length argument

def add(n,p,*value):
    print(n)
    print(value)
    print(p)

add(22,34,67,34)    