#polymorphism 

class bird:

    def flying(self):
        print(" i can fly")

    def walking(self):
        print("i can walk")

class sparrow(bird):    
    pass

class penguin(bird):
    def flying(self):
        print("i ca not fly")

p = penguin()
p.flying()
p.walking()

b=bird()
b.flying()