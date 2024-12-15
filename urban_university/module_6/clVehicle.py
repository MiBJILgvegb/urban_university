class Vehicle:
    
    __COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']
    def __init__(self,owner,model,color,ep):
        self.owner=owner
        self.__model=model
        self.__color=color
        self.__engine_power=ep
    def check_color(self,color):
        i=0
        finded=False
        while(not finded and i<len(self.__COLOR_VARIANTS)):
            if(color.lower()==self.__COLOR_VARIANTS[i].lower()):
                finded=True
                break
            i+=1
        return finded
    def get_model(self):
        return f"Модель: {self.__model}."
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}."
    def get_color(self):
        return f"Цвет: {self.__color}."
    def print_info(self):
        print(self.get_model(),self.get_horsepower(),self.get_color(),f"Владелец: {self.owner}.")
    def set_color(self,color):
        if(not self.check_color(color)):
            print(f"Нельзя сменить цвет на {color}.")
            return False
        self.__color=color
        return True