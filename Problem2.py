# Take user input to enter the sides of the triangle then find the area of that triangle.

a = int(input("Enter side og the triangle:: "))
b = int(input("Enter side og the triangle:: "))
c = int(input("Enter side og the triangle:: "))
s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5 
# both ways in which we can print our result
print("Area of triangle is = ",area) 
print("Area of triangle is %0.1f" %(area))
