import threading
import time

def write_words(word_count, file_name):

    with open(file_name,"w+") as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

start=time.time()
print("функции")
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
fin = time.time()
print(f"Процесс занял {fin-start} времени")

start=time.time()
print("Потоки")
thread1=threading.Thread(target=write_words,args=(10, "example1.txt"))
thread1.start()
thread1.join()

thread2=threading.Thread(target=write_words,args=(30, "example2.txt"))
thread2.start()
thread2.join()

thread3=threading.Thread(target=write_words,args=(200, "example3.txt"))
thread3.start()
thread3.join()

thread4=threading.Thread(target=write_words,args=(100, "example4.txt"))
thread4.start()
thread4.join()

fin = time.time()
print(f"Процесс занял {fin-start} времени")