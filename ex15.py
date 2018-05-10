# this allows us to import the module called 'argv' to take in an argument in the bash
from sys import argv
# here we are defining what these arguments are called and how many arguments the argv will be taking. in this case its 2.
script, filename = argv
# here we are assigning a variable called 'txt' to the action of actually opening the second argument in the argv
txt = open(filename)
# some simple printing + formatting
print(f"Here's your file {filename}:")
# .read seems to automatically parse the text file and return the documents contents
print(txt.read())
# printing the prompt and then accepting a new argument of the user input
txt.close()
print("Type the filename again:")
file_again = input("> ")
# reading the new arguement passed and still opening a file, this is a refactor that allowed me to remove a line of code and just chain .read to it.
txt_again = open(file_again).read()
# i wonder what you can pass .read....
print(txt_again)
