# setting an integer var
types_of_people = 10
# here we are still setting a string var, and using string interpolation with 'f'. No parens needed
x = f"There are {types_of_people} types of people." # 1/4
# two vars set as strings
binary = "binary"
do_not = "don't"
# again, setting a var using string interp
y = f"'Those who know {binary} and those who {do_not}.'" # 2/4
# now we are printing both vars. that used string interp
print(x)
print(y)
# this showcases printing the vars. parens required as we are actually printing them
print(f"I said: {x}") # 3/4
print(f"I also said: {y}") # 4/4
# setting a var as a Boolean value
hilarious = False
# this is interesting. for some reason we include the brackets. if we exclude the brackets the boolean doesn't hit
joke_evaluation = "Isn't that joke so funny?! {}"
# now we are priting the vars and .format is a method that must be similar to 'f' but won't work w/o straight strings
print(joke_evaluation.format(hilarious))
# this showcases concatenation use
w = "This is the left side of..."
e = "a string with a right side."
# this showcases concatenation use
print(w + e)
