def plus(*value):
    sum=0
    for number in value:
        sum+=number
    print("sum =",sum)

plus(21,25,26,2365)        
 
 # here *value is variable length argument

def add(n,p,*value):
    print(n)
    print(value)
    print(p)
add(23,56,78,35)  

#local and global variable 

total=20

def value():
    total=0
    print("total_local=",total)

value()
print("total_global=",total)    

# if change the global variable value in function

total=20

def change_value():
    global total
    total=0
    print("total_local=",total)

change_value()
print("total_global=",total)   