# coding: cp1251
def GetMultipliedDigits(number):
    if(len(str(number))==1):
       return number
    else:
        return int(str(number)[0])*GetMultipliedDigits(int(str(number)[1:]))

def Main():
    number=input("������� �����: ")
    print(GetMultipliedDigits(number))