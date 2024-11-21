immutable_var=(0,[1,2],3.4,'56',False)
print("immutable_var: ",immutable_var)
# 'tuple' object does not support item assignment
#элементы кортежа не меняются
#хотя можно сделать кортеж с единственным элементом-массивом и менять сколько угодно....
#immutable_var[0]=1
immutable_var[1][0]=0
print("changed immutable_var: ",immutable_var)
mutable_list=[0,1,2,3]
print("immutable_list: ",mutable_list)
mutable_list[0]=-1
mutable_list[1]=-2
print("immutable_list: ",mutable_list)