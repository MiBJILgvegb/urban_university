from module_6.clAnimal import *
import random
class Bird(Animal):
    beak = True
    def lay_eggs(self):
       print(f"Here are(is) {random.randint(0,4)} eggs for you")
       return