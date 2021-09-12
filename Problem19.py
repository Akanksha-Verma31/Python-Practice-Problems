# WAP to print fibonacci no. or term entered by user
def fibo(n):
    a = 0
    b = 1
    if n<0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
         for i in range(3,n):
            c = a + b
            a = b
            b = c
            return b

n = int(input("Enter: "))
print(fibo(5))
