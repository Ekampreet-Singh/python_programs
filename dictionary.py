# cmp is not run in python3

paragraph=input("Enter the paragraph:")

words = paragraph.split()

counter = {}

for word in words:
    if word in counter:
        counter[word] = counter[word]+1

    else:
        counter[word] = 1

for key,value in counter.items():
    print(key,"=",value)           

