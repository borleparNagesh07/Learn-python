# Nested loops: Nested loops are loops inside another loop. They allow you to iterate over a sequence of sequences, such as a list of lists or a grid-like structure.

# Nested Loop to Print a Rectangular Pattern:
# Example: Print a 3x3 rectangular pattern using nested loops
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # Move to the next line after each row

# Nested Loop to Print a Triangle Pattern:
# # Example: Print a right-angled triangle pattern using nested loops

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after each row

# Printing a multiplication table (up to 5x5)

for i in range(1, 6):  # Outer loop (for rows)
    for j in range(1, 6):  # Inner loop (for columns)
        print(i * j, end="\t")  # Print product of i and j with a tab space
    print()  # Print a new line after each row

# Write a nested loop that prints a square pattern of stars (asterisks).

n = 5  # Size of the square (5x5)

for i in range(n):  # Outer loop for rows
    for j in range(n):  # Inner loop for columns
        print("*", end=" ")  # Print a star with a space
    print()  # Move to the next line after each row

# Write a nested loop to print a right-angled triangle of numbers in ascending order.

n = 5  # Height of the triangle

num = 1  # Starting number

for i in range(1, n + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns (1 to i)
        print(num, end=" ")  # Print the current number
        num += 1  # Increment the number after each print
    print()  # Move to the next line after each row

# Create a nested loop that prints a hollow square pattern of stars (asterisks).

n = 5  # Size of the square (5x5)

for i in range(n):  # Outer loop for rows
    for j in range(n):  # Inner loop for columns
        # Print a star for the border and space for the hollow part
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space for the hollow part
    print()  # Move to the next line after each row


# Write a nested loop to calculate and print the sum of numbers from 1 to 5 using nested iteration.

sum_total = 0  # Initialize the sum to 0

# Outer loop for numbers 1 to 5
for i in range(1, 6):
    # Inner loop to add numbers from 1 to i
    for j in range(1, i + 1):
        sum_total += j  # Add the current number to the sum

print("The sum of numbers from 1 to 5 is:", sum_total)

# Create a nested loop to print the reverse of the multiplication table from 1 to 5 (up to 10 times each).

for i in range(5, 0, -1):  # Outer loop for numbers 5 to 1 (reverse)
    for j in range(10, 0, -1):  # Inner loop for numbers 10 to 1 (reverse)
        print(i * j, end="\t")  # Print the product of i and j
    print()  # Move to the next line after each row

# Write a nested loop that prints a right-angled triangle of stars (asterisks).

n = 5  # Height of the triangle

for i in range(1, n + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for printing stars
        print("*", end=" ")  # Print a star with a space
    print()  # Move to the next line after each row

# Create a nested loop to find and print prime numbers from 2 to 20.

for num in range(2, 21):  # Outer loop to iterate over numbers from 2 to 20
    is_prime = True  # Assume the number is prime
    for i in range(2, num):  # Inner loop to check divisibility
        if num % i == 0:  # If num is divisible by any number other than 1 and itself
            is_prime = False  # Set is_prime to False if it's not prime
            break  # No need to check further, break the inner loop
    if is_prime:  # If is_prime is still True, the number is prime
        print(num)

# Write a nested loop that prints a diamond pattern of stars (asterisks).

n = 5  # Number of rows for the top half of the diamond

# Upper half of the diamond
for i in range(1, n + 1):  # Outer loop for the upper half
    for j in range(n - i):  # Inner loop for spaces before the stars
        print(" ", end="")  # Print space
    for j in range(2 * i - 1):  # Inner loop for printing stars
        print("*", end="")  # Print star
    print()  # Move to the next line after each row

# Lower half of the diamond
for i in range(n - 1, 0, -1):  # Outer loop for the lower half
    for j in range(n - i):  # Inner loop for spaces before the stars
        print(" ", end="")  # Print space
    for j in range(2 * i - 1):  # Inner loop for printing stars
        print("*", end="")  # Print star
    print()  # Move to the next line after each row

# Create a nested loop to find and print the factorial of numbers from 1 to 5.

for num in range(1, 6):  # Outer loop for numbers from 1 to 5
    factorial = 1  # Initialize the factorial to 1 for each number
    
    # Inner loop to calculate the factorial of the current number
    for i in range(1, num + 1):
        factorial *= i  # Multiply factorial by i for each iteration
    
    print(f"Factorial of {num} is: {factorial}")


