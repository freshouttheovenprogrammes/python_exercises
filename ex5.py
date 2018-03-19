# in python, format string == rubys string interpolation. difference is, we use { } instead of #{ }
my_name = "Zac Palmquist"

my_age = 27

my_height = 6.15

my_weight = 165

my_eyes = 'brown'

my_teeth = 'white' # on good days

my_hair = 'brown'

# interesting that I must format the string with the letter f beforehand.
print(f"Lets talk about {my_name}.")
# attempt to see what happens if I don't use the formatting 'f'
# print("Lets talk about {my_name}.")
# we get Lets talk about Zac Palmquist. vs Lets talk about {my_name}.
print(f"He's {my_height} feet tall.")
print(f"He's {my_weight} pounds heavy.")
print("That's not that heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are colored {my_teeth}, on a good day. Depends on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add my age: {my_age}, my height: {my_height} and my weight: {my_weight}, I get {total}") # total should be 198.15
