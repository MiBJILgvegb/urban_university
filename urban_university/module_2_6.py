import random

def GenerateRightCode():
    return random.randint(3,20)

def IsDivider(source,divider):
    return source%divider==0

def FindTerms(source):
    terms=[]
    for i in range(1,source-1):
        for j in range(i+1,source):
            if(IsDivider(source,i+j)):
                terms.append([i,j])

    return terms

def GetLeftCode(source):
    res=""
    for i in range(0,len(source)):
        for j in range(0,len(source[i])):
            res=res+str(source[i][j])

    return res

rightCode=GenerateRightCode()
print(rightCode,GetLeftCode(FindTerms(rightCode)))