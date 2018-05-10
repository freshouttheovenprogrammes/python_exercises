from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.\nIf you don't want that, hit CTRL-C (^C).\nIf you do want that, hit RETURN.")
input("?")

print("Opening the file...")
target = open(filename, 'w') # passing the 'w' lets us write to the file

print("Truncating the file. Goodbye!")
target.truncate() # this is cool because it basically deletes everything in there so I can overwrite it!

print("Now I'm going to ask you for three lines.")
#
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
#
print("I'm going to write these to the file.")
#
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#
print("And finally, we close it.")
target.close() # still a little lost on this front
