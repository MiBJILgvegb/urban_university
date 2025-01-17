import threading,time,random

class Bank:
    def __init__(self):
        self.balance=random.randint(0,1000)
        self.lock=threading.Lock()
    def deposit(self):
        for i in range(100):
            dep=random.randint(50,500)
            self.balance+=dep
            print(f"Пополнение: {dep}. Баланс: {self.balance}")
            if (self.balance >= 500 and self.lock.locked()):
                self.lock.release()
            time.sleep(0.001)
    def take(self):
        for i in range(100):
            dep = random.randint(50, 500)
            print(f"Запрос на {dep}")
            if (self.balance >= dep):
                self.balance -= dep
                print(f"Снятие: {dep}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
print(f"Стартовый баланс: {bk.balance}")

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')