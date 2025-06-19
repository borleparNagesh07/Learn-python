# Conditional expressions allow your program to make decisions based on conditions.

# if condition:
#     # Code executes if condition is True
# elif another_condition:
#     # Code executes if another_condition is True
# else:
    # Code executes if no conditions are True

a = int(input("Enter your age: "))

# If else statement
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

else:
    print("You are below the age of consent")


print("End of Program")

# Example 1: Checking if a number is positive or negative

num = int(input("Enter a number: "))  # User input

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Checking if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Explanation:

#     % is the modulus operator (finds remainder).
#     If num % 2 == 0, it's even; otherwise, it's odd.

# USING LOGICAL OPERATOR
# Example 3: Using 'and' with boolean variables
a = True
b = False

result = a and b
print(result)  # Output: False

# Example 4: Using 'and' with expressions
x = 10
y = 5

result = (x > 0) and (y < 10)
print(result)  # Output: True

result = (x > 0) and (y > 10)
print(result)  # Output: False

# Example 5: Using 'or' with boolean variables
a = True
b = False

result = a or b
print(result)  # Output: True

# Example 6: Using 'or' with expressions
x = 10
y = 5

result = (x > 0) or (y < 10)
print(result)  # Output: True

result = (x < 0) or (y > 10)
print(result)  # Output: False


# Example 7: Using 'not' with boolean variable
a = True

result = not a
print(result)  # Output: False

# Example 8: Using 'not' with an expression
x = 10
y = 5

result = not (x > y)
print(result)  # Output: False

result = not (x < y)
print(result)  # Output: True

