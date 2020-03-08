# if user enter the string and your program want integer value then program show the error

try:
    age = int(input("Enter the age :"))
    print("your age is :",age )
except Exception as e:
    print(e)

# next program
try:
    n1 = int(input("enter the number 1:"))
    n2 = int(input("enter the number 2:"))
    
    print("didision =",n1/n2)    
except ZeroDivisionError:
    print("please don't enter 0")    

except ValueError:
    print("please enter numeric value")    


