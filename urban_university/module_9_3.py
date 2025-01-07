first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result=(len(z1)-len(z2) for z1,z2 in zip(first,second) if len(z1)!=len(z2))
second_result=(len(first[i])==len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))