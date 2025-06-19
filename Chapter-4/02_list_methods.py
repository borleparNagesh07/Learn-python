friends = ["Apple","Nagesh","Akash", "Rohan", 0.345 , 7 , False]

# Modifying elements
friends[0] = "Mango"

print(friends)

# Adding elements
friends.append("date")
print(friends)

# Removing elements
friends.remove("Akash")
print(friends)

# Slicing
print(friends[1:])

L1 = [12,9,24,15,19,21,18,1,6]

print(L1)

# sort() Sorts the list in place (i.e., it modifies the original list) in ascending order by default.

L1.sort()
print(L1)

# reverse() Reverses the order of the list in place.It will not sort,simply reverses the order of current elements
 
L1.reverse()
print(L1)

# Append() Adds a single element to the end of list

L1.append(28)
print(L1)

# insert() inserts an element at a specified.The first argument is the index where the element should be inserted, and the second argument is the element itself.

L1.insert(3,44)
print(L1)

# pop()  Removes and returns an element at a given index. If no index is specified, it removes and returns the last element.

L1.pop(3)
print(L1)

# remove() Removes the first occurrence of a specified value from the list.If the value is not found in the list, a ValueError is raised

L1.remove(6)
print(L1)