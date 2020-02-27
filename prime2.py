n =int(input("Enter the number:"))

prime=0

for i in range(2,n//2):
    if n%i==0:
        print(n,"is divisible by",i)
        prime=1

if prime==0:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")    
