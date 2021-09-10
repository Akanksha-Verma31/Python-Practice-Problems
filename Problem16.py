# write a program to check whether a numer is prime or not
n = int(input("enter the number: "))
flag = 0
if n == 1 or n == 0:
    flag = 1
for i in range(2, n):
    if(n % i == 0):
        flag = 1
if flag == 1:
    print("not prime")
else:
    print("prime")
