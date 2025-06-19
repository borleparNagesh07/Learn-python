# FOR LOOP : In Python, a for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. The loop continues until all items in the sequence have been processed.

# The basic syntax of a for loop in Python is as follows:
# for item in sequence:
    # Code block to be executed for each item in the sequence

# Example 1:Printing numbers from 1 to 5 using a for loop?
for num in range(1, 6):
    print(num)

# Example:2:Use a for loop to calculate the sum of numbers from 1 to 10.

total_sum = 0

for i in range(1, 11):  # Loop through numbers from 1 to 10
    total_sum += i  # Add the current number to the total sum

print("The sum of numbers from 1 to 10 is:", total_sum)

# EX: Write a for loop to print each character in the string "Hello".

for char in "Hello":
    print(char)

# EX:Write a for loop to print the first 10 even numbers.

for i in range(2, 21, 2):  # Start at 2, end at 20, step by 2
    print(i)

# EX:Create a for loop that doubles each number in the sequence: 1, 2, 3, 4, 5.

for i in range(1, 6):  # Loop through numbers 1 to 5
    print(i * 2)  # Double the current number and print it
