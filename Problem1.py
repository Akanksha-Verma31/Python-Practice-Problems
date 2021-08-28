# Take user input to enter any number. Then find the square root of that number.

x = int(input("Enter the number you want to square:: "))
square = x**0.5
# both ways in which we can print our result
print("Square of {} is = ".format(x), square)
print("square root of %0.3f is %0.3f" %(x,square))
