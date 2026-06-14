class Instagram:
    posts={}
    def __init__(self,name,age,gender,user_name,password):
        self.name=name
        self.age=age
        self.gender=gender
        self.__user_name=user_name
        self.__password=password
        self.friends=[]
        self.following=0
        self.followers=0
        self.logged=False
    def login(self,username,password):
        if self.__user_name==username and self.__password==password:
            self.logged=True
            print("Login Successful")
        else:
            print("Invalid Password")
    def logout(self):





