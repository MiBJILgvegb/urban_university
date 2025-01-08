from random import choice

class MysticBall:
    def __init__(self,*answ):
        self.words=answ
    def __call__(self):
        return choice(self.words)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,"w") as f:
            for ds in data_set:
                f.write(str(ds)+"\n")

    return write_everything

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda l1,l2:l1==l2, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())