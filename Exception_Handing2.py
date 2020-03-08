# if you want the code is exicut whose in the program in any condition like any error in program then code is exxicut
try:
    with open('ashu.txt','r') as f:
        f.write("wronge file")
except:
    print("please create a file")

finally:
     print("program is end")            