
#that is use in calculate the length of any string.

str1="   the crazy programmer the the the"
length=len(str1)
print(type(length))
print("length",length)

#that is used in remove whitespaces from both side,starting and ending.

str2=str1.strip()
print(str1)
length=len(str2)
print("length",length)
print(str2)
 
#that is used in write string in lowwer/upper latters.

str2=str1.lower()
str3=str1.upper()
print(str2)
print(str3)

#that is used in replace words in string and you enter how many time replace words.

str2=str1.replace("the","a",3)
print(str1)
print(str2)
