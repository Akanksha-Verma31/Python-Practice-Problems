# Take age of 4 persons and find the greatest among them.

# METHOD 1: nested if 

age1 = int(input("Enter age of 1st person: "))
age2 = int(input("Enter age of 2nd person: "))
age3 = int(input("Enter age of 3rd person: "))
age4 = int(input("Enter age of 4th person: "))

if age1>age2:
    if age1>age3:
        if age1>age4:
            print(age1," is greatest among the four entered.")
if age2>age1:
    if age2>age3:
        if age2>age4:
                print(age2, " is greatest among the four entered.")
if age3>age1:
    if age3>age2:
        if age3>age4:
            print(age3," is greatest among all four entered.")
if age4>age1:
    if age4>age2:
        if age4>age3:
            print(age4," is greatest among all four entered.")

# METHOD 2: using if-elif-else
age1 = int(input("Enter age of 1st person: "))
age2 = int(input("Enter age of 2nd person: "))
age3 = int(input("Enter age of 3rd person: "))
age4 = int(input("Enter age of 4th person: "))

if age1>age2 and age1>age3 and age1>age4:
    print(age1," is greatest.")
elif age2>age1 and age2>age3 and age2>age4:
    print(age2," is greatest.")
elif age3>age1 and age3>age2 and age3>age4:
    print(age3," is greatest.")
else:
    print(age4," is greatest.")
    
# METHOD 3: using logical operator
age1 = int(input("Enter age of 1st person: "))
age2 = int(input("Enter age of 2nd person: "))
age3 = int(input("Enter age of 3rd person: "))
age4 = int(input("Enter age of 4th person: "))
if (age1>age2 and age1>age3 and age1>age4):
    print(age1," is greatest.")
if (age2>age1 and age2>age3 and age2>age4):
    print(age2," is greatest.")
if (age3>age1 and age3<age2 and age3>age4):
    print(age3," is greatest.")
if (age4>age1 and age4<age2 and age4>age3):
    print(age4," is greatest.")
    
# METHOD 4: using a built-in function max()
age1 = int(input("Enter age of 1st person: "))
age2 = int(input("Enter age of 2nd person: "))
age3 = int(input("Enter age of 3rd person: "))
age4 = int(input("Enter age of 4th person: "))

greatest_age = max(age1,age2,age3,age4)
print(greatest_age, " is the greatest.")

# METHOD 5: using loop and max()
ages = []
i = 1
for i in range (4):
    age = int(input("Enter age : "))
    ages.append(age)
print("Greatest among {} is {}.".format(ages,max(ages)))

