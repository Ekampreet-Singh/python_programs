n=int(input("enter the number"))  

if n%3 == 0:
    if n%5 == 0:
        print("crazy programer")

    else:
        print("crazy")    

elif n%5 == 0:
    print("programmer")        

else:
    print("the crazy programmer")    