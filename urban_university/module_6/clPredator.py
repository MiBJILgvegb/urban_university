from module_6.clAnimal import *
from module_6.clFlower import *

class Predator(Animal):
    def eat(self, food):
        #if(isinstance(food,Flower)):
        #    print(f"{food.name} - не еда.")
        #    return False
        if(not food.edible):
            print(f"{self.name} не стал есть {food.name}.")
            self.alive=False
            return False
        print(f"{self.name} съел {food.name}.")
        self.fed=True
        return True