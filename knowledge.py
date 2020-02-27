import wikipedia

name = input("enter a name:")

if name !=  'ashu':
    print(wikipedia.summary(name, sentences=3))
else:
    print(" you are a great tatti man")