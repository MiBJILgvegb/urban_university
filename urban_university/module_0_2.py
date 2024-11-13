#1st program
def FirstTask():
    print("1st task",(9**0.5)*5,"",sep="\n")

#2nd program
def SecondTask():
    print("2nd task",(9.99>9.98)&(1000!=1001),"",sep="\n")

#3rd program
def ThirdTask():
    i=2*2+2
    j=2*(2+2)
    print("3rd task",i,j,i==j,"",sep="\n")

#4th program
def ForthTask():
    s='123.456'
    print("4th task",int((float(s)%1)*10),"",sep="\n")

#main
FirstTask()
SecondTask()
ThirdTask()
ForthTask()