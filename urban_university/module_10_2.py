import threading,time

class Knight(threading.Thread):
    def __init__(self,name,power,daemon=False):
        super().__init__(name=name,daemon=daemon)
        #self.name=name
        self.power=power
        self.enemies_count=100
    def fighting(self):
        start=round(time.time())
        now=start
        while self.enemies_count:
            time.sleep(1)
            self.enemies_count-=self.power
            now=round(time.time())
            print(f"{self.name} сражался {now-start} дней..., осталось {self.enemies_count} воинов.")

        return now-start
    def run(self):
        print(f"{self.name}, на нас напали!")
        print(f"{self.name} одержал победу спустя {self.fighting()} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()