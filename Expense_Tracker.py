#Python Variables and Types
user_name= "Asha"
category="Travel"
amount= 850.0
is_essential= True

#Input and Print Statements
user_name= input("Enter your name: ")
category= input("Enter the category of expense: ")
amount= float(input("Enter the amount spent: "))
print(f"hello {user_name}!")
print(f"category of expense: {category}")
print(f"amount spent: {amount}")

#Arithmatic Operations
service_fee= 50.0
total_amount= amount + service_fee
print(f"Service fee: ₹{service_fee:.2f}")
print(f"Total amount spent including service fee: ₹{total_amount:.2f}")

#if-else Statements
essential_answer= input("Is this expense essential? (yes/no): ")
if essential_answer.lower() == "yes":
    is_essential= True
    print("This expense is essential.")
else:
    is_essential= False
    print("This expense is not essential.")


#Expressions and Comparisons
if amount > 1000 and is_essential:
    print("priority: Review this essential High-value expense.")
else:
    print("priority: Standard Review.")