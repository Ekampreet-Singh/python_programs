# multi level inheritance

class Parent:
    parent_property = ''
    __parent_private_property = 1000 

    def parent_method(self):
        print("example parent method")

class SubParent(Parent):
    def sub_parent_method(self):
        print("example sub parent method")

class child(SubParent):
    pass

c = child()
c.sub_parent_method()
c.parent_method()