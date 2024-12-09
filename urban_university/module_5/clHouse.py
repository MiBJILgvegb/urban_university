class House:
    houses_history=[]
    #5.4
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __del__(cls):
        print(f"{cls.name} снесён, но он останется в истории");
    #5.1
    def __init__(self,name,number_of_floors):
        if(not(type(name) is str))or(len(str(name))<=0):
            print("Имя объекта должно быть строкой длиннее нуля символов.")
            return None
        self.name = name
        
        if(not(type(number_of_floors) is int))or(number_of_floors<=0):
            print("Количество этажей должно быть числом больше нуля.")
            return None
        self.number_of_floors = number_of_floors
    #5.2
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    #5.3
    def __lt__(self, other):
        if(isinstance(other,type(self))):
            return self.number_of_floors<other.number_of_floors
        return None
    def __le__(self, other):
        if(isinstance(other,type(self))):
            return self.number_of_floors<=other.number_of_floors
        return None
    def __eq__(self, other):
        if(isinstance(other,type(self))):
            return self.number_of_floors==other.number_of_floors
        return None
    def __ne__(self, other):
        if(isinstance(other,type(self))):
            return self.number_of_floors!=other.number_of_floors
        return None
    def __gt__(self, other):
        if(isinstance(other,type(self))):
            return self.number_of_floors>other.number_of_floors
        return None
    def __ge__(self, other):
        if(isinstance(other,type(self))):
            return self.number_of_floors>=other.number_of_floors
        return None

    def __add__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=self.number_of_floors + other
            return self
        return None
    def __sub__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=self.number_of_floors - other
            return self
        return None
    def __mul__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=self.number_of_floors * other
            return self
        return None
    def __matmul__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=self.number_of_floors @ other
            return self
        return None
    def __truediv__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=self.number_of_floors / other
            return self
        return None
    def __floordiv__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=self.number_of_floors // other
            return self
        return None
    def __mod__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=self.number_of_floors % other
            return self
        return None
    def __divmod__(self, other):
        if(isinstance(other,int)):
            #self.number_of_floors=self.number_of_floors % other
            return {(self.number_of_floors / other),(self.number_of_floors % other)}
        return None
    def __pow__(self, other):
        if(isinstance(other,int)):
            self.number_of_floors=pow(self.number_of_floors,other)
            return self
        return None
    def __pow__(self, other,module):
        if(isinstance(other,int)):
            self.number_of_floors=pow(self.number_of_floors,other) % module
            return self
        return None

    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __rsub__(self, other):
        return self.__sub__(other)
    def __isub__(self, other):
        return self.__sub__(other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        return self.__mul__(other)
    def __rmatmul__(self, other):
        return self.__matmul__(other)
    def __imatmul__(self, other):
        return self.__matmul__(other)
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    def __itruediv__(self, other):
        return self.__truediv__(other)
    def __rfloordiv__(self, other):
        return self.__floordiv__(other)
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
    def __rmod__(self, other):
        return self.__mod__(other)
    def __imod__(self, other):
        return self.__mod__(other)
    def __rdivmod__(self, other):
        return self.__divmod__(other)
    def __idivmod__(self, other):
        return self.__divmod__(other)
    def __rpow__(self, other):
        return self.__pow__(other)
    def __rpow__(self, other,module):
        return self.__pow__(other,module)

    #5.1
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