# write a program to create a dictionary of telugu words with values as their english translation.Provide user with an option to look it up!

words = {
    "sahayam": "Help",
    "kurchi": "Chair",
    "pilli": "Cat",
    "thappu": "mistake",

}

word = input("Enter the word you want meaning of: ")

print(words[word])

# Write a program to input eight numbers from the user and display all the unique number(once)

s = set()
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)

# Can we have a set with 18(int) and "18"(str) as a values in it?

s= set()

s.add(18)
s.add("18")

print(s)

# what will be length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add("20.0") # length pf s after these operations?

print(len(s))

# s ={} what is the type of 's'

s = {}

print(type(s))

# Create an empty dictionary allow 4 friends to enter their favourite language as values and use keys as their name.Assume that the names are unique?

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)

# If names of 2 friends and languages  are same; what will be the program

# The values entered later will be updated

# Can you change the values inside a list which is contained in set s

s = {8,7,12,"Nagesh",[1,2,3]}

s[4][0] = 9
print(s)