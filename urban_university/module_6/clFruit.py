from module_6.clPlant import *

class Fruit (Plant):
    def __init__(self,name,edible=True):
        if(not isinstance(name,str)):
            print("Имя должно быть строкой.")
            return None
        self.name=name
        self.edible=edible