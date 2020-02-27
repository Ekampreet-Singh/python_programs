# create list 

my_list=["ashu",22,330,12.3,'d']
print(type(my_list))
print(my_list)

# looping over each element using for and while loop

i=0
while i<len(my_list):
    print(my_list[i])
    i+=1

for item in my_list:
    print(item)

# list through index or Accessing a pafticular item from a list

print(my_list[0])
print(my_list[4])
# creating list from a string using list constructor

str1="ekmpreet"
list1=list(str1)
print(list1)

#creating the list from string's split() metod merging two lists

str1="ekmpreet is a student"
print(str1.split())

list1=[12,3,4,5]
list2=[12,6,4,7,]
print(list1+list2)

# add item in list using append() method 

my_list=["mskdlj",";asjco","jcih","chmnjk"]
print(my_list)
my_list.append("ashu")
print(my_list)

#Accessing a particular part of list using slices
print(my_list[0:4])
print(my_list[-2:])
print(my_list[-3:-1])

#reversing a list 

my_list.reverse()
print(my_list)
