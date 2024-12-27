import os,time

def prn(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            #print(root,dirs,file)
            filepath = os.path.join(root, file)
            filetime = os.stat(filepath).st_mtime
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.stat(filepath).st_size
            parent_dir = root
            print(f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}")
    return

prn(os.getcwd())