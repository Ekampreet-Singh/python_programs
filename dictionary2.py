# cmp is not run in python3

paragraph=input("Enter the paragraph:")

words = paragraph.split()

counter = {}

for word in words:
    if word in counter:
        counter[word] = counter[word]+1

    else:
        counter[word] = 1

word_list=list(counter.keys())
frequency=list(counter.values())

max_value=max(frequency)
index_of_frequency=frequency.index(max_value)

worrd_max = word_list[index_of_frequency]

print('"{}" is the most used word which is used {} times in the paragraph'.format(worrd_max,max_value))
