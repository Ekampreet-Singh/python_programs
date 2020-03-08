class Person:
    def __init__(self,name,father_name):
        self.name = name
        self.f_name= father_name

    def gerenal_info(self):
        print("name ={}\n father's name ={}".format(self.name,self.f_name))


class student(Person):
    def __init__(self,name,father_name,roll_no):
        super().__init__(name,father_name)
        self.roll_no = roll_no

    def student_info(self):
        print("name = {}\n father's name = {}\n roll_no ={}".format(self.name,self.f_name,self.roll_no)) 


s= student("Ekam","mr Harzindra Singh",17)
s.gerenal_info()
s.student_info()