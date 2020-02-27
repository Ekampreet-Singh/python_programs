# find the sum of all items of any list ,tuple,etc

def plus(n1):
    sum=0
    for item in n1:
        sum=sum+item

    return(sum)

numbers=[25,36,48,25]        
total=plus(numbers)
print(total)

# find the minimum value of list,tuple,etc

def minimum(n2):
    min=n2[0]

    for number in n2:
        if number<min:
            min=number

    return(min)

number=[2,5,25,2635,25]
min=minimum(number)
print(min)        

# find the maximum value of list,tuple,etc

def maximum(n2):
    max=n2[0]

    for number in n2:
        if number>max:
            max=number

    return(max)

number=[2,5,25,2635,25]
max=maximum(number)
print(max)        