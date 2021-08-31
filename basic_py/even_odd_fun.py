def is_even(num):
    if (num%2)==0:
        return True
    else:
        return False

y = int(input("y"))
x = is_even(y)
if x==True:
    print('even')
else:
    print('odd')
