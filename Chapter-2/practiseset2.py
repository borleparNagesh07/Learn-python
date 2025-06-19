# write a python program to add two nunmbers
a = 10

b = 20

print (a + b)

# write a python program to find remainder when a number is divided by b

a = 47

b = 5

print ("Remainder when a is divided by b is ", a % b)

# check the type of the variable assigned using input() function

a = input("Enter the value of a ")

print(type(a))

# use comparision operator to find out whether a given variable a is greater than 'b' or not a=34,b=80

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("a is greater than b is", a > b)

# write a python program to find average of two numbers entered by the users.

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))

print("The average of these two numbers is", (a+b)/2)

# write a python program to calculate square of a number entered by the user

a = int(input("Enter your number is: "))

print("The square of a number is", a**a)

# Define a variable value and assign any numerical value to it. Ask the user to input a new value. Update the variable value with the new input and print the updated value.

# Define a variable value and assign a numerical value to it
value = 10

# Ask the user to input a new value
new_value = input("Enter a new value: ")

# Update the variable value with the new input (convert to a number)
value = float(new_value)  # Use float to handle decimals; use int if you want integers

# Print the updated value
print(f"The updated value is: {value}")