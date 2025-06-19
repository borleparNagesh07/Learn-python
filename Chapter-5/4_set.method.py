# Set Methods and Operations

# Creating a set with initial elements
numbers = {1, 2, 3, 4, 5}
# Creating an empty set (note: {} creates an empty dictionary)
empty_set = set()

# Adding Elements: add(): Adds an element to the set.
numbers.add(6)
print(numbers)  # Output might be: {1, 2, 3, 4, 5, 6}

# remove(): Removes a specific element; raises a KeyError if the element is not found.

numbers.remove(3)
print(numbers) #-> {1, 2, 4, 5, 6}

# pop(): Removes and returns an arbitrary element from the set.

element = numbers.pop()
print(element)  # Could be any element from the set.
print(numbers)

# clear(): Removes all elements from the set.

numbers.clear()
print(numbers)  # Output: set()

# Union: Combines elements from two sets (all unique elements).

set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)

# Alternatively: union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection: Returns elements common to both sets.

intersection_set = set_a.intersection(set_b)
# Alternatively: intersection_set = set_a & set_b
print(intersection_set)  # Output: {3}

