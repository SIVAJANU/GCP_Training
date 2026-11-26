# for loop vs while loop
# for loop is used when we know the number of iterations
# while loop is used when we don't know the number of iterations
# while syntax:
# while condition:  
    #block of code to be executed
    #counter += 1
name=input("Enter your name: ")
count=0
while count < len(name):
    if name[count]=='v':
        print('v is present in the name')
    count+=1
        # print('a is present in the name')
        # print(f"The letter 'v' appears {count} times in the name.")
    