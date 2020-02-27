n=int(input("enter the number:"))

answer=[]
for i in range(2,n+1):
    if n%i==0:
        answer.append(i)

print("number that can fully divide",n,"=",answer)        