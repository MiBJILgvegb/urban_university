class IncorrectVinNumber(Exception):
    #message0="Некорректный тип vin номер"
    #message1="Неверный диапазон для vin номера"
    def __init__(self,message):
        self.message=message
class IncorrectCarNumbers(Exception):
    #message0="Некорректный тип данных для номеров"
    #message1="Неверная длина номера"
    def __init__(self,message):
        self.message=message
class Car:
    __vin=0
    __numbers=""
    model=""
    def __init__(self,model,vin,number):
        if(self.__is_valid_vin(vin)):
            self.__vin=vin
        if(self.__is_valid_numbers(number)):
            self.model=model
    def __is_valid_vin(self,vin_number):
        if(not isinstance(vin_number,int)):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if(vin_number<1000000 or vin_number>9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True
    def __is_valid_numbers(self,numbers):
        if(not isinstance(numbers,str)):
            raise IncorrectVinNumber("Некорректный тип данных для номеров")
        if(len(numbers)!=6):
            raise IncorrectVinNumber("Неверная длина номера")
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')