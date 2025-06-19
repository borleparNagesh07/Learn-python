# write a python program to display a user entered name followed by good afternoon using input() function

name = input("Enter your name: ")

print(f"Good Afternoon, {name} ")

print("Good Afternoon " + name + "")

# write a program to fill in a letter template given below with name and date

letter = '''Dear <|Name|>,
 you are selected !
 <|Date|>'''

print (letter.replace("<|Name|>", "Nagesh").replace("<|Date|>", "12 feb 2025"))

# write a program to detect double spaces in a string

name = "Nagesh is a good boy and "

print (name.find(""))

# write a program to detect single spaces in a string

name = "Nagesh is a good  boy and "

print (name.replace("  "," "))
print (name) # Strings are immutable which means that you cannot change them by rumming functions on them

# write a program to format the following letter using escape sequence character, \n,\t,\"\"

letter = "Dear Nagesh,\n\tThis python course is nice.\n\"Thanks\"!"

print (letter)