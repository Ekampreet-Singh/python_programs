n=int(input("enter the number:"))

even=[]
odd=[]

for number in range(1,n+1):
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)    


print("even number=",even)
print("odd numbre=",odd)
