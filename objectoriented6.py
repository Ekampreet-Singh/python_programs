class car:

    speed = 100

    def __init__(self):
        self.current_speed = 0


    def accelerate(self):
        print("accelerating")
        self.current_speed +=10
        print("new speed",self.current_speed)

    def breaks(self):
        print("stopped")
        self.current_speed=0

class HondaCity(car):

    speed = 240

car1= HondaCity()

print(car1.current_speed)
car1.accelerate()
car1.breaks()
print(car1.current_speed)