first=input("first=")
second=input("second=")
third=input("third=")

out=0
if(first==second==third):
    out=3
elif(first==second)or(second==third)or(first==third):
    out=2

print(out)
