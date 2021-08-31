# logical operators help you build logic in a program even further
# what if you want to combine some booleans
# we have an and operator, or operator and a not operator we can use them wisely

# now lets see what  logical operators do
# and (both have to be true and the result will be true)
print(True and True)
print(False and True)
print(False and False)
# or operators, one of them have to be true then the result will be true
print(True or False)
print(False or False)
# not operator inverts the result, if it is False it gives true and vice versa
print(not (True))
# Now lets use them in real programming

is_engine_running = True
is_water_flowing = True
are_lights_on = True
reactor_status = False

if (is_engine_running and is_water_flowing and are_lights_on):
    reactor_status = True
    print("Reactor running perfectly ...")
elif (is_engine_running or are_lights_on):
    print("lights are on or the engine is running")
elif (is_water_flowing):
    print("water is flowing")
else:
    print("All statements are FALSE")
# another usefull example , even or odd
num = int(input("please enter a number"))
if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")
# if you dont understand it yet, we will go through all these things in this sections project
# comparison + logical = used a lot

num = 33
# number that is between two numbers
if(num >= 23 and num <= 55):
    print("its in the range")
else:
    print("its not in the range")
