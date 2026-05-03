#problem 2
#user input
time = float(input('Enter travel time (hrs): '))
average_speed = float(input('Enter average speed (mph): '))

#formula
distance = average_speed * time

#display result
print("Distance_traveled: ", distance, "miles")
# Run program using table data
print("Route Comparison:")

#local
local_distance = 1.00 * 30
print("Local distance:", local_distance)

#parkway
parkway_distance = 0.88 * 40
print("Parkway distance:", parkway_distance)

#highway
highway_distance = 0.87 * 55
print("Highway distance:", highway_distance)