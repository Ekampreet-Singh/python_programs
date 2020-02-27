# create len function for list

def length(list1):
    i=0
    for item in list1:
        i+=1
                         
    return (i)    

list2=[22,54,53,554,36,39]    
total=length(list2)
print(total)

# create len function for string


def length2(str1):
    i=0
    for item in str1:
        i+=1

    return (i)    

str2="Ekampreet"    
total=length2(str2)
print(total)