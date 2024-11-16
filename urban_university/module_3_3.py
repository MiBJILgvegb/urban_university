# coding: cp1251
def PrintParams(a = 1, b = 'строка', c = True):
    print(f"a={a}\nb={b}\nc={c}",end="\n\n")

def Main():
    print("Вызов PrintParams")
    PrintParams()
    PrintParams(0)
    PrintParams(0,'asdf')
    PrintParams(0,'asdf',False)
    PrintParams(b=25)
    PrintParams(c=[1,2,3])

    print("Распаковка")
    values_list=[0, 'строка0', False]
    values_dict={'a' : 1, 'b' : 'строка', 'c' : True}
    PrintParams(*values_list)
    PrintParams(**values_dict)

    print("Распаковка2")
    values_list_2 =[0, 'строка1']
    PrintParams(*values_list_2,42)