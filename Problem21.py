# WAP to print fibonacci series upto n terms using recursion
def recur_fibo(num):
    if num <= 1:
        return num
    else:
        return(recur_fibo(num-1) + recur_fibo(num-2))

terms = int(input("How many terms? "))

if terms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(recur_fibo(i))
