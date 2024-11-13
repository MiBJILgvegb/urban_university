def GetMatrix(n, m, value):
    res=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(value)
        res.append(row)

    return res

result1 = GetMatrix(2, 2, 10)
result2 = GetMatrix(3, 5, 42)
result3 = GetMatrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
