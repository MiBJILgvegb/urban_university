first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result=[len(f) for f in first_strings if len(f)>4]
second_result=[(f1,f2) for f1 in first_strings for f2 in first_strings if(len(f1)==len(f2))]
third_result={f:len(f) for f in first_strings+second_strings if(len(f) % 2 == 0)}

print(first_result)
print(second_result)
print(third_result)