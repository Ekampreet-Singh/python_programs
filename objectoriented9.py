#hierarchical inherirtance 1 base class , multiple child class

class Parent:
    parent_property = ''
    __parent_private_property = 1000 

    def parent_method(self):
        print("example parent method")

class child(Parent):
    def child_1_method(self):
        print("child 1")

class child2(Parent):
    def child_2_method(self):
        print("child 2")        

c = child2() 
c.child_2_method       