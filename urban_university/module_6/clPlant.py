﻿class Plant:
    edible = False

    def __init__(self,name,edible=False):
        if(not isinstance(name,str)):
            print("Имя должно быть строкой.")
            return None
        self.name=name
        self.edible=edible
    def __str__(self):
        return self.name