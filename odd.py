limit=int(input("Enter the number:"))

for i in range(1,limit+1):
    if i%2==0:
        continue
    print(i, end=" ")