class House:
    def __init__(self,name,number_of_floors):
        if(not(type(name) is str))or(len(str(name))<=0):
            print("Имя объекта должно быть строкой длиннее нуля символов.")
            return None
        self.name = name
        
        if(not(type(number_of_floors) is int))or(number_of_floors<=0):
            print("Количество этажей должно быть числом больше нуля.")
            return None
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if(not(type(new_floor) is int)):
            print("Количество этажей должно быть числом больше нуля.")
            return False
        if(new_floor<1)or(new_floor>self.number_of_floors):
            print("Такого этажа не существует.")
            return False

        for i in range(1,new_floor+1):
            print(i)
        
        return True