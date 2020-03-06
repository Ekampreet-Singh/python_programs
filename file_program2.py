with open('example.txt','w') as f:
    f.write("ashu is here")
    f.write("i'm here")
    print("ekampreet",file=f)
    
 
 with open('example.txt','r') as file1:
     show = file1.read()
     print(show)   