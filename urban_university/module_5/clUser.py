class User:
    nickname=""
    password=0
    age=0

    def __new__(cls, *args):
        nickname=""
        password=0
        age=0

        return object.__new__(cls)
    def __del__(self):
        nickname=""
        password=0
        age=0

    def __init__(self,name,pwd,age):
        if(isinstance(name,str)):
            self.nickname=name
        if(isinstance(pwd,int)):
            self.password=pwd
        if(isinstance(age,int)):
            self.age=age

    def __str__(self):
        return self.nickname