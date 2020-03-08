#hierarchical inherirtance 1 base class , multiple child class

class Parent:
    parent_property = ''
    __parent_private_property = 1000 

    def parent_method(self):
        print("example parent method")

class Parent2:
    def parent2_method(self):
        print("Parent 2 method")

class child(Parent,Parent2):
    pass      

c = child() 
c.parent2_method