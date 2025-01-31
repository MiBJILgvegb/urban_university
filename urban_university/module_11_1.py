import multiprocessing,time,threading

def read_info(name):
    all_data=[]
    with open(name,"r") as f:
        all_data.append(f.readline())

if __name__ == '__main__':
    filenames = [f'./module_11/1/file {number}.txt' for number in range(1, 5)]
    start=time.time()
    for filename in filenames:
        read_info(filename)
    end=time.time()
    print(f"line - {end-start}")

    start=time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, filenames)
    end=time.time()
    print(f"multiproc - {end-start}")