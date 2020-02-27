list1=[54,56,55,2,68,223,255]

even=[]
odd=[]

for number in list1:
    if number%2==0:
        even.append(number)

    else:
        odd.append(number)

print("List=",list1)
print("odd list=",odd)
print("Even list=",even)
print("sum of odds=",sum(odd))
print("sum of even=",sum(even))

        