#file1 = open("example.txt","r")
#show = file1.read()
#print(show)
#print("closed", file1.closed)
#file1.close()

#print("closed", file1.closed)

##new program
#file1 = open("example.txt","r")
#show = file1.read()
#print(show)
#print( file1.mode)
#print(file1.name)
#file1.close()
# new style

with open('example.txt','r') as file1:
    show = file1.read()
    print(show)
    print(file1.mode)
    print(file1.name)
    print(file1.closed)
print(file1.closed)
print("end")




