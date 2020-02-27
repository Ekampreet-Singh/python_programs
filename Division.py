print("This is perform persentage of high school of a student")
marks=int(input("Enter the numbers"))

if(marks<601):
  
  if(marks>390):
    print("you get first division")
  elif(marks>300):
    print("you get sceond division") 
  elif(marks>198):
    print("you get third division")
  else:
      print("you are fail")
    
  print("your marks in presentage",marks/6)

else:
  print("you enter the wronge value ")  