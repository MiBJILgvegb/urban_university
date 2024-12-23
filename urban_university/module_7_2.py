import io,os.path

def file_exists(file_name):
    return os.path.exists(file_name)
def custom_write(file_name, strings):
    file_path=os.path.dirname(os.path.realpath(__file__))+"\\"+file_name
    strings_positions={}
    if(not file_exists(file_path)):
        f=open(file_path,"a")
        f.close()
    with open("file_path", "w") as f:
        i=1
        for s in strings:
            key = (i, f.tell())
            f.writelines(s)
            strings_positions[key]=s
            i+=1
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)