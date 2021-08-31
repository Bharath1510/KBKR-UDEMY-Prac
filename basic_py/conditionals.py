# conditionals are very important in programming, they let us enforce logic
# the boolean data type
#  we didn't discuss earlier but now is time
# booleans show things as true or false
is_the_door_open = False
is_everything_normal = True
# you first if  statement
if is_everything_normal:
    print("everything is normal")
# you can also use an else statement for the other wise option
if is_the_door_open:
    print("the door is open")
else:
    print("the door is not open")
# make sure that the indentation is right other wise it wont work

# if else chaining
if is_everything_normal:
    print("everything is normal")
elif is_the_door_open:
    print("everything is not normal and the door is open")
else:
    print("everything is not normal and the door is closed")
# you can write as many if else statements as you want we will discuss them more in the enxt video
# these are vital for writing any logic in your program
