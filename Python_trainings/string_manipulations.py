list_1=['siva', 'kumar', 'vijay']
list_2=[11,33,55,99,99,100,11,1000,999,999]
list_4=[1,1,1,1,1,1,1,1,1,1]
print(f"list_4 before we extend it with list_2: {list_4}")
list_1.append(list_2)
print(list_1) # Output: ['siva', 'kumar', 'vijay', [11, 33, 55, 99]]
list_4.extend(list_2)
 # Output: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 33, 55, 99]
print(f"list_4 after we extend it with list_2: {list_4}") # Output: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 33, 55, 99]
# list_3=list_1+list_2
# print(list_3)
list_5=[]
for i in list_4:
    if i not in list_5:
        list_5.append(i)
print(f"list_5 which is de-duplicated list_4: {list_5}") # Output: [1, 11, 33, 55, 99]

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
    # Output: 0, 1, 1, 2, 3, 5, 8

# string manipulations
'''siva123
ravi456
harish789'''

str_1='siva123'
# split it if we have numeric values
print(str_1.count('a'))

#Functions
list_1=[1,2,3,10]
print(f'Sum of numbers in list_1 {sum(list_1)}')


    



