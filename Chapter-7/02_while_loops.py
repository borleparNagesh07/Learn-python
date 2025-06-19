# In Python, a "while loop" is used to repeatedly execute a block of code as long as a specified condition is True. The loop continues until the condition becomes False.

# Note:
# while loops are useful when you don't know the exact number of iterations needed in advance, and the loop's termination depends on a certain condition being met. Be cautious while using while loops to avoid infinite loops and ensure your loop eventually terminates.

# while condition:
    # Code block to be executed while the condition is True


# Example 1: Printing numbers from 1 to 5 using a while loop
i = 1

while(i < 5):
    print(i)
    i +=1 # or i = i + 1 

# Explanation:It's important to ensure that the condition in the while loop eventually becomes False; otherwise, the loop will run indefinitely, leading to an infinite loop.

# Example 2 : Finding the sum of numbers from 1 to 10 using a while loop
num = 1
sum_of_numbers = 0

while num <= 10:
    sum_of_numbers += num
    num += 1

print("Sum of numbers from 1 to 10:", sum_of_numbers)

# Create a while loop that calculates the sum of numbers from 1 to n, where n is the input.

n = int(input("Enter a number: "))  # Take input from the user
sum_of_numbers = 0
i = 1

while i <= n:
    sum_of_numbers += i
    i += 1

print("The sum of numbers from 1 to", n, "is:", sum_of_numbers)

# Write a while loop that prints even numbers from 2 to 10.

i = 2  # Start with the first even number
while i <= 10:
    print(i)
    i += 2  # Increment by 2 to get the next even number

# Create a while loop that keeps prompting the user for a number until they enter a negative number.

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        print("You entered a negative number. Exiting the loop.")
        break  # Exit the loop when a negative number is entered

# Write a while loop that counts down from 10 to 1 ?

i = 10  # Start with 10
while i >= 1:
    print(i)
    i -= 1  # Decrement by 1

# Write a while loop that calculates the factorial of a given number.

n = int(input("Enter a number: "))  # Take input from the user
factorial = 1
i = 1

while i <= n:
    factorial *= i  # Multiply the current value of factorial by i
    i += 1  # Increment i

print("The factorial of", n, "is:", factorial)

# Create a while loop that prints the Fibonacci series up to n.

n = int(input("Enter a number: "))  # Take input from the user
a, b = 0, 1  # Initialize the first two Fibonacci numbers

while a <= n:
    print(a, end=" ")  # Print the current Fibonacci number
    a, b = b, a + b  # Update a and b to the next two Fibonacci numbers

# Write a while loop that reads numbers from the user until they enter the number 0. Then, it prints the sum of all the entered numbers.

total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    
    total_sum += number  # Add the entered number to the sum

print("The sum of all entered numbers is:", total_sum)

# Create a while loop that prints the square of numbers from 1 to 5.

i = 1  # Start with 1
while i <= 5:
    print(i ** 2)  # Print the square of the current number
    i += 1  # Increment i to move to the next number

