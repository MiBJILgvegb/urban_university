﻿def personal_sum(numbers):
    result=[0,0]
    for num in numbers:
        try:
            result[0]+=num
        except(TypeError):
            result[1]+=1
            print(f"Некорректный тип данных для подсчёта суммы - {num}")
    return result
        
def calculate_average(numbers):
    try:
        ps=personal_sum(numbers)
        return ps[0]/(len(numbers)-ps[1])
    except(ZeroDivisionError):
        return 0
    except(TypeError):
        print("В numbers записан некорректный тип данных")
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать