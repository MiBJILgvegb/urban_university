print("Dictionary")
my_dict={'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict['Vasya'])
print(my_dict.get('Vasya1'))
my_dict['Kamila']= 1981
my_dict['Artem']= 1915

print(my_dict)
my_dict_pop=my_dict.pop('Artem')
print(my_dict)
print("!Deleted! element: ",my_dict_pop)
print()

print("Sets")
my_set={1,1, 'Vasya','Vasya', 42.314}
print(my_set)
my_set.add(0)
my_set.add(0.1)
print(my_set)
