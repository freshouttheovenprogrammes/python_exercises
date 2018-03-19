# in python, format string == rubys string interpolation. difference is, we use { } instead of #{ }
name = "Zac Palmquist"

age = 27

height = 6.15
height_inch = height * 12
height_centimeter = round((height_inch * 2.54), 2)

weight = 165
kilo_convert = 2.20462
weight_in_kilo = round((165 / kilo_convert), 4)

eyes = 'brown'

teeth = 'white' # on good days

hair = 'brown'

# interesting that I must format the string with the letter f beforehand.
print(f"Lets talk about {name}.")
# attempt to see what happens if I don't use the formatting 'f'
# print("Lets talk about {name}.")
# we get Lets talk about Zac Palmquist. vs Lets talk about {name}.
print(f"He's {height} feet tall.")
print(f"He's {height_centimeter} centimeters tall")
print(f"He's {weight} pounds heavy.")
print(f"He weighs {weight_in_kilo} kilos.") # answer should be 74.8427
print("That's not that heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are colored {teeth}, on a good day. Depends on the coffee.")

total = age + height + weight
print(f"If I add my age: {age}, my height: {height} and my weight: {weight}, I get {total}") # total should be 198.15

# challenge
# Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do
# not just type in the measurements. Work out the math in Python.
