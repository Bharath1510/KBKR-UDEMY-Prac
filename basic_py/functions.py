# functions are very important, for now you have writen code in a full application
# in real life we use functions are logic blocks that can be used anywhere
# for example we wrote how to tell whether some number is even or odd but we have to write that everytime
# like all the functions you have seen so far we can define our own as well
# function structure
# def function_name ( parameters):
#      some operations done with or without parameters
#     return some output or none
#
#
def sum_numbers(num1, num2):
    return num1+num2


sum_of_numbers = sum_numbers(2, 3)
print(sum_of_numbers)
# you can do many useful things with functions


def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False


print("725 is even: " + str(is_even(725)))
# as you will see later functions are very important in implementing complex programs and
# make our lives much more easier
# recursion
# dont want to go deep as it is an advanced topic but recursions are efficient than loops for repetitive things
# just one example

# in recursion we call the function itself in the function body
# we need an end condtion for recursion as well


def count_down(x):
    if(x == 1):
        print(x)
        return 1
    print(x)
    return count_down(x - 1)


count_down(9)
# lambda expressions are anonymous functions, they are simply functions without names
# they are not accessible afte rtheir creation and have no identity// like a function has
# x = lambda arg1: arg1 show in terminal
