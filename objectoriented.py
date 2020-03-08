class car():
    color='black'
    speed=60

    def increase_speed(self):
        self.speed+=20

    def breaks(self):
        self.speed=0  
tesla =car()
tesla.color='red' 
tesla.autodrive='on'

print(tesla.speed)
tesla.increase_speed()
print(tesla.speed)
tesla.breaks()
print(tesla.speed)
print(tesla.autodrive)