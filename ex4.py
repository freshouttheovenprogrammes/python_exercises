# here I am stating any time we call the variable 'cars' it will be equal to 100
cars = 100
# same thing here
space_in_a_car = 4.0
# same thing here
drivers = 30
# same thing here
passengers = 90
# finally, variance. we are now subtracting the values of the variables 'cars' and 'passengers'
cars_not_driven = cars - drivers
# redundant but, now cars_driven = the same value as drivers themselves
cars_driven = drivers
# more math! now we are multiplying cars_driven * space_in_a_car to find how many people could fit by carpooling
carpool_capacity = cars_driven * space_in_a_car
# lets see how many people can fit per car!
average_passengers_per_car = passengers / cars_driven

# using a variable in this fashion means that it can change as needed to reflect 'how many cars there are'
print("There are", cars, "cars available.")
# same thing here, now we take on new variables to show new results reflecting drivers available
print("There are only", drivers, "drivers available." )
# now we can see how many cars not driven, thanks to combining cars - passengers!
print("There will be", cars_not_driven, "empty cars today.")
#
print("We can transport", carpool_capacity, "people today.")

print("We have", passengers, "passengers to carpool today.")

print("We need to put about", average_passengers_per_car, "in each car.")
