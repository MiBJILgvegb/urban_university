import module_6 as m6

a1 = m6.clPredator.Predator('Волк с Уолл-Стрит')
a2 = m6.clMammal.Mammal('Хатико')
p1 = m6.clFlower.Flower('Цветик семицветик')
p2 = m6.clFruit.Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)


print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)