# if read and write both are perform in one file 

with open('exal.txt','w+') as f:
    f.write("ashu ")
    show = f.read()
    print(show)

# if you want to sve the new data in a file and don't want delete old data

with open('exal.txt','a+') as f:
    f.write("ashu ")
    f.write("\n ekampreet")    
    show = f.read()
    print(show)
