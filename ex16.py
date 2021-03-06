from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.\nIf you don't want that, hit CTRL-C (^C).\nIf you do want that, hit RETURN.")
input("?")

print("Opening the file...")
target = open(filename, 'w') # passing the 'w' lets us write to the file

print("Truncating the file. Goodbye!")
# target.truncate() # this is cool because it basically deletes everything in there so I can overwrite it!
# Its also not needed since the arguement of 'w' in open just replaces it anyways!!

print("Now I'm going to ask you for three lines.")
#
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
#
print("I'm going to write these to the file.")
#
new = "\n"
target.write(line1 + new + line2 + new + line3 + new)
#
print("And finally, we close it.")
target.close() # still a little lost on this front
