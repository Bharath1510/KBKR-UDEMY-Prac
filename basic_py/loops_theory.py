# loops help you do some things again and again as long a condition is true
# loops also help you traverse an iterable object like an array
# lets start with a while
# declate loop variable
# while <condition depending on variable>:
#   update variable
#
#  a loop as a initializer
i = 0
# a condition
while(i < 10):
    print("i = "+str(i))
    # an update
    i += 1
# an infinite loop case
# while (True):
    # print("i is true")

# other type of loop is a for loop, a little more neat than a while loop
# for <iterating_number_variable> in <a range or an array>
#       <body>
#
#
for i in range(10):
    print("i = "+str(i))
    # range returns a sequence of numbers
# range( start, stop, step)
# if you give only one parameter to the function its step is 1 and starts from 0
for i in range(4, 10):
    print("i = "+str(i))

for i in range(4, 10, 2):
    print("i = "+str(i))
# iterating over an array
# for loops are used to iterate over arrays
numbers = [1234, 421, 3, 124, 12, 312, 41, 23, 214, 21, 3]
for num in numbers:
    print(num)
# for loops can also be used to iterate over dictionaries
dictionary = {
    "name": "jacky",
    "state": "stable"
}
for key in dictionary:
    print(dictionary[key])
