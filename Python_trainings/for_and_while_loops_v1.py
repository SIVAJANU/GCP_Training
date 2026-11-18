name='Siva vara prasad'
list_1=name.split(' ')
print(list_1)
print(name.upper())
print(name[0:10:4])
print(name.count('a',0,10))
count=0
for i in name:
    if i=='v':
        count+=1         
        # print('a is present in the name')
        # print(f"The letter 'v' appears {count} times in the name.")
print(f"V appeared {count} times in the name.")