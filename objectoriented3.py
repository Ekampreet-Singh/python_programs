# staticmethod
class car():
    color='black'
    speed=60


    @staticmethod
    def class_function():
        print("this is a class function")    
       

    def increase_speed(self):
        self.speed+=20

    def breaks(self):
        self.speed=0  
tesla =car()
tesla.color='red' 
tesla.autodrive='on'
car.class_function()

print(tesla.speed)
tesla.increase_speed()
print(tesla.speed)
tesla.breaks()
print(tesla.speed)
print(tesla.autodrive)