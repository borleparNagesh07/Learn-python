# prob-1 write a poem
# This is the whispers of the morning
print('''The sun peeks through the silver mist,
A golden kiss, a lover's twist.
The world awakens, soft and slow,
As rivers of light begin to flow.

The trees stretch high with arms of grace,
Their branches dance in nature’s trace.
Birds sing songs of joy anew,
While dew upon the grass is blue.

The sky, a canvas, painted bright,
In shades of rose and lavender light.
A breeze, so gentle, stirs the air,
Carrying dreams beyond compare.

In this moment, pure and still,
Time seems to pause, and hearts refill.
For every dawn, a chance to find,
The peace that lives within the mind.

So let the morning whispers speak,
Of quiet strength, of being meek.
And with each step, embrace the day,
As light and love both lead the way.''')

# Problem-3 Installing external module and perform an operation
# step-1 firstly importing text to speech Module
# step-2 pip install pyttsx3
# step-3 after entering import module we have to enter this all
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text,Hello Myself borleparnagesh")
engine.runAndWait()

# prob-4 python program to print the contents of a directory using os module.Search online for the function which does that?

import os

# Specify the directory you want to list
directory_path = '/'
 # Replace with your desired path or leave empty for current directory

#List all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)

# prob-5 Adding comments to the lines of python
print("hello world")