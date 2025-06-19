a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

# count(x)
# Returns the number of times x appears in the tuple.
no = a.count(45)
print(no)

# index(x[, start[, end]])
# You can access individual elements of a tuple using an index (zero-based).
i = a.index(3424)
print(i)

# Length len()
# The built-in function len() returns the number of items in a tuple.
print(len(a))

#  Slicing
# Slicing allows you to retrieve a range of elements from the tuple

print(a[1:])
print(a[:4])

# Concatenation
# You can combine two or more tuples using the + operator.

b = (5,99,100)
c = a + b
print(c)

# Repetition repeat
# Repeating a tuple multiple times can be done with the * operator.

print(b * 5)