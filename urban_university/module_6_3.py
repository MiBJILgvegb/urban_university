from module_6.clDuckbill import *

db = Duckbill("Duckbill",10)

print(db.live)
print(db.beak)


db.speak()
db.attack()


db.move((1, 2, 3))
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()