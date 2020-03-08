# if you want to know where is the carzer in your file

with open('example.txt','r') as f:
    content = f.read(6)
    print(content)
    print(f.tell())
    print(f.read(5))
    f.seek(0,0)
    print(f.read(6))