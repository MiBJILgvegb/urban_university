from module_6.clAnimal import *
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dzm=1
        if(dz<0):
            dzm=-1
        self._cords[2]-=int(dz*dzm*(self.speed/2))
        return