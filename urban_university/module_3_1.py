# coding: cp1251

def CountCalls():
    global calls
    calls += 1

def StringInfo(string):
    CountCalls()
    return {len(string),string.upper(),string.lower()}

def IsContains(string,stringsList):
    CountCalls()
    i=0
    result=False
    while(i<len(stringsList)):
        if(string.lower() in stringsList[i]):
            result=True
            break
        i+=1
    return result

calls=0
strings=[]
i=int(input("�������� ���-�� �����: "))
for i in range(0,i):
    strings.append(StringInfo(input()))

print(f"���� �� ��������� �������: {strings}")
print(IsContains(input("����������� ������: "),strings))
print(calls)
