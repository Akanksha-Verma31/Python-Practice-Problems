# write a function to find the sum of 1,2,3,4 using arbitrary arguments
def sum(*num):
    sum1 = 0
    for a in num:
        sum1 = sum1 + a
    print(sum1)
    
sum(1,2,3,4)
