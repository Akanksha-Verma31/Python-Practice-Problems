# WAP to find factorial of a number

def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        print("Invalid input")
        
    else:
        return(num*factorial(num-1))
    
x = int(input("Enter a number: "))
fact = factorial(x)
print(f"Factorial of {x} is ", fact)
