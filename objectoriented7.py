#single level inheritance -1 base class -1 child class

class Parent:
    parent_property =''
    __parent_private_property = 1000 

    def parent_method(self):
        print("example parent method")

class child(Parent):
    pass

c=child()
c.parent_method()       

  