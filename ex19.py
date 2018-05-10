def cheese_and_crackers(cheese_count, boxes_of_crackers):
    cheese_count = input("How many types of cheese do you want? ")
    boxes_of_crackers= input("How many boxes of crackers will you have? ")
    print(f"Damn! You have {cheese_count} types of cheese and {boxes_of_crackers} boxes of crackers?! Goddamn!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def another_function(programming_language, hours):
    print(f"Man I have been writing some {programming_language} for like {hours} hours!")

# print("We can just give the function numbers directly")
# cheese_and_crackers(20, 30)


# print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)


# print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Lets see how your function holds up pimp!")
another_function("ruby", 10**10)
