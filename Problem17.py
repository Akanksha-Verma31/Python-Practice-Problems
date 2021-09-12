# write a function to find the largest of three numbers entered by the user
def largest(a,b,c):
    if a>b and a>c:
        print(f"{a} is largest")
    elif b>c and b>a:
        print(f"{b} is largest")
    else:
        print(f"{c} is largest")
        
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
largest(num1,num2,num3)
    
