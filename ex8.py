formatter = "{} {} {} {}" #not sure what this does yet

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# to me, this is an example of parallel assignment. the variables change each time that we run the lines of code as we set the variables to something different
# on each line
