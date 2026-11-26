def sum_list_elm(list_1):
    sum_elm=0
    for i in list_1:
        sum_elm=sum_elm+i
    return print(f'sum of list of elements is {sum_elm}')
sum_list_elm([11,10,11,10,100])






def sum_num(a,b):
    res=a+b
    return res

sum_num(5,5)

var_1=100+sum_num(10,10)
print(var_1)

#print(print(1))

def sum_num_arg(*args):
    res=sum(args)
    return res

var_1=100+sum_num_arg(10,10,100,101,1000,100000)
print(var_1)

# ananymous function or lambda functions
#syntax ---->lambda x,y:x+y

v=lambda x,y:x+y 
print(v(5,5))

