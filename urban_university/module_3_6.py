def calculate_structure_sum(data,summ=0):
    #print(data)
    if(isinstance(data,tuple)):
        summ=calculate_structure_sum(list(data),summ)
    elif(isinstance(data,list)):
        for list_elem in data:
            summ=calculate_structure_sum(list_elem,summ)
    elif(isinstance(data,dict)):
        for dict_key in data.keys():
            summ=calculate_structure_sum(dict_key,summ)
            summ=calculate_structure_sum(data[dict_key],summ)
    elif(isinstance(data,set)):
        summ=calculate_structure_sum(data.pop(),summ)
    elif(isinstance(data,int)):
        summ+=data
    elif(isinstance(data,str)):
        summ+=len(data)
    else:print(type(data))
    #print(f"summ={summ}")
    return summ

data_structure = [
[1, 2, 4],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
(
    (), 
    [
        {
            (2, 'Urban', 
             ('Urban2', 30)
            )
        }
    ]
)
]

print(data_structure)
print("summ=",calculate_structure_sum(data_structure))