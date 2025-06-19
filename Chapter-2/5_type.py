# Type of conversion
# Implict conversion

a = 100  #Integer Type

b = "Nagesh"  # String Type

c = "32.5" # when we type an int or float value in double quotes it will convert it into string

d = 32.5 # Float type

print(type(d))

# Explicit Type Conversion

e = 100 
f = "Nagesh"

e = str(e)  # converting int no to str
f = float(e) # converting int no to float
g = int(f)  # converting int str to int

print (type(e))
print (type(f))
print (type(g))
