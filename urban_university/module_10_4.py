import threading,time,random,queue
from queue import Queue

class Guest(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)
    def run(self):
        time.sleep(random.randint(3,10))

class Table:
    def __init__(self,num,guest=None):
        self.number=num
        self.guest=guest
    def is_free(self):
        return self.guest is None
    def guest_flee(self):
        self.guest=None
    def guest_arrive(self,guest):
        self.guest=guest
        self.guest.start()

class Cafe:
    def __init__(self,*tables):
        self.tables=tables
        self.free_tables_count=len(self.tables)
        self.queue=Queue()
    def get_free_table(self):
        finded,i=False,0
        while (i<len(self.tables) and not finded):
            if(self.tables[i].is_free()):
                finded=True
            else:
                i+=1
        return self.tables[i]
    def guest_arrival(self, *guests):
        for guest in guests:
            if(self.free_tables_count>0):
                free_table=self.get_free_table()
                free_table.guest_arrive(guest)
                self.free_tables_count-=1
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")
    def next_guest(self,table):
        if (not self.queue.empty()):
            guest = self.queue.get()
            self.guest_arrival()
            print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
    def discuss_guests(self):
        while (not self.queue.empty() or self.free_tables_count<len(self.tables)):
            for table in self.tables:
                if(not table.is_free()):
                    if(not table.guest.is_alive()):
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        table.guest_flee()
                        print(f"Стол номер {table.number} свободен")
                        self.free_tables_count+=1
                        self.next_guest(table)
                else:
                    self.next_guest(table)
            print(f"Свободно столов: {self.free_tables_count}\nПосетителей в очереди: {self.queue.qsize()}")
            time.sleep(1)
        print("Все поели и разошлись")

tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
