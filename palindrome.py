n=int(input("enter the number:"))
temp=n
reversed=0

while(temp>0):
    remainder=temp % 10
    temp //= 10

    reversed= reversed * 10 + remainder
     
if n==reversed:
    print("number is a palindrome")    

else:
    print("number is not a palindrome")    