class account:
    def __init__(self,username,password,name,phone_number):
         self.user_name=username
         self.password=password
         self.name=name
         self.phone_number=phone_number
         self.posts=[]

         self.logged_in = False


    def login(self,username,password):
        if username == self.user_name:
            if password == self.password:
                print("logged in")
                self.logged_in = True
            else:
                print("password incorrect") 
        else:
            print("username not found")
    
    def post(self,p):
        if self.logged_in:
            self.posts.append(p)
            print(p, "[posted]") 
        else:
            print("please login to post ")        
    
    def my_wall(self):
        print("\n posts")
        if self.logged_in:
            i=1
            for post in self.posts:
                print(i, post)
                i+=1
        else:
            print("please login to see the posts")        

    def get_info(self):
        if self.logged_in == True:
            print("name = {}, phone_number = {}".format(self.name,self.phone_number))

        else:
            print("please login first") 


    def logout(self):
        if self.logged_in == False:
            print("you are already logged out")      
        else:
            self.logged_in = False
            print("logged out")        

user1 = account(username="user1", password="pass1", name="ashu", phone_number="4552555225")
user2 = account(username="user2", password="pass2", name="ekam", phone_number="4845855665")


user1.login(username="user1", password="pass1")
user1.post("how are you")
user1.post("hellow world")
user1.my_wall()
user1.get_info()
user1.logout()
