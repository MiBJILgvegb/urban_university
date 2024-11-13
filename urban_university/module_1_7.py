def Calc(grades):
    res=0
    for g in grades:
        res+=g
    return res/len(grades)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
studentsList=sorted(list(students))

result={}
i=0
for stud in studentsList:
    result[stud]=Calc(grades[i])
    i+=1

print(result)