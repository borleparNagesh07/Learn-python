marks = {
    "Nagesh": 100,
    "Indra": 56,
    "Varad": 23
}

# items(): Returns a view object of (key, value) pairs.
print(marks.items())

# keys(): Returns a list containing dictionary's keys.
print(marks.keys())

# values(): Returns a view object of values.
print(marks.values())

# update({}): updates the dictionary with supplied/new key value pairs
marks.update({"Nagesh":95, "Sunitha":100})
print(marks)

print(marks.get("Nagesh2")) # Prints None
print(marks["Nagesh2"]) # Returns an error