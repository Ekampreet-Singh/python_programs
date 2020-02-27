# with count method

paragraph=input("Enter the paragraph:")
word=input("Enter word:")

list1=paragraph.split()
occurance=list1.count(word)

print('"{}"have appeared {} times in a given paragraph'.format(word,occurance))

#with for loop 

occurance=0

for w in list1:
    if w==word:
        occurance+=1

print('"{}"have appeared {} times in a given paragraph'.format(word,occurance))        
