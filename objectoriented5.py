class Game:

    def __init__(self):
        self.__score = 0

    def getscore(self):
        print("score :" , self.__score)     

    def got_one_point(self):
        self.__score +=1  

p = Game()
p.__score=10
p.got_one_point()
p.got_one_point()
p.got_one_point()
p.getscore()     