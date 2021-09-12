# WAP to check if the entered number is palindrome
def reverse(num):
    temp = num
    rev = 0
    while(num>0):
        remain = num % 10
        rev = rev * 10 + remain
        num = num//10
    if (temp == rev):
        print(f"{temp} is a palindrome!")
    else:
        print(f"{temp} isn't a palindrome!")

n = int(input("Enter number: "))
reverse(n)
