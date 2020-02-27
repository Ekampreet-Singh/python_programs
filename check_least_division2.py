n=int(input("Enter the "))
ans=0
for i in range(2,n):
    if n%i==0:
        ans=i
print("Answer {} is divided by {}".format(n,ans))
