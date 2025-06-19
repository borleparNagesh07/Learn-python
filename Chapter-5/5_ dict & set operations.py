# This example creates a dictionary of student details, accesses and updates values, and then uses several dictionary methods:

# Dictionary Example: Student Details

# Create a dictionary with initial student details
student = {
    'name': 'John Doe',
    'age': 21,
    'major': 'Computer Science'
}
print("Initial student dictionary:", student)

# Accessing values using key indexing and get()
print("Student Name (indexing):", student['name'])
print("Student Age (get):", student.get('age'))
print("Student GPA (get with default):", student.get('gpa', 'Not Available'))

# Adding a new key-value pair and updating an existing one
student['gpa'] = 3.8       # Add GPA
student['age'] = 22        # Update age
print("\nAfter adding/updating entries:", student)

# Removing entries with pop() and del
removed_gpa = student.pop('gpa')
print("\nRemoved GPA:", removed_gpa)
del student['major']
print("After removing 'major':", student)

# Using keys(), values(), and items() methods
print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Updating dictionary using update()
additional_info = {'city': 'New York', 'graduated': False}
student.update(additional_info)
print("\nAfter update:", student)

# Clearing all items from the dictionary
student.clear()
print("\nAfter clearing, student dictionary:", student)

# What This Code Does:

#     Creates a dictionary with key-value pairs.
#     Accesses values using both indexing and the get() method (with a default value).
#     Adds a new entry and updates an existing one.
#     Removes entries using pop() and del.
#     Demonstrates keys(), values(), and items() methods.
#     Uses the update() method to merge another dictionary.
#     Clears the dictionary with clear().

# This example creates two sets representing two groups of numbers and then performs several set operations:

# Set Example: Number Groups

# Create two sets with some overlapping elements
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

# Add and remove elements in a set
set_a.add(9)
print("\nSet A after adding 9:", set_a)

set_a.remove(3)  # remove() will raise an error if the element does not exist
print("Set A after removing 3:", set_a)

set_a.discard(10)  # discard() does nothing if the element is absent
print("Set A after discarding 10 (non-existent):", set_a)

# Set operations: union, intersection, difference, and symmetric difference
union_set = set_a.union(set_b)  # or set_a | set_b
print("\nUnion of Set A and Set B:", union_set)

intersection_set = set_a.intersection(set_b)  # or set_a & set_b
print("Intersection of Set A and Set B:", intersection_set)

difference_set = set_a.difference(set_b)  # or set_a - set_b
print("Difference (Set A - Set B):", difference_set)

symmetric_diff_set = set_a.symmetric_difference(set_b)  # or set_a ^ set_b
print("Symmetric Difference between Set A and Set B:", symmetric_diff_set)

# Clearing the set
set_a.clear()
print("\nSet A after clearing:", set_a)

# What This Code Does:

#     Creates two sets with some overlapping numbers.
#     Demonstrates adding an element with add(), removing with remove(), and safely discarding an element with discard().
#     Performs set operations:
#         Union: Combines all unique elements.
#         Intersection: Finds common elements.
#         Difference: Finds elements present in one set and not in the other.
#         Symmetric Difference: Finds elements that are in one set or the other, but not both.
#     Clears a set with clear().