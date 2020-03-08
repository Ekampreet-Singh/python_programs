with open('example.txt','w') as f:
    f.write("ashu is here\n")
    f.write("i'm here\n")
    print("ekampreet",file=f)
    
 
with open('example.txt','r') as file1:
     show = file1.read(15)
     print(show)   


#if file is not exist then file is auto matic exist
     
with open('ashu.txt','w') as f:
    f.write("ashu is here\n")
    f.write("i'm here\n")
    print("ekampreet",file=f)
    
 
with open('example.txt','r') as file1:
     show = file1.read(15)
     print(show)   
