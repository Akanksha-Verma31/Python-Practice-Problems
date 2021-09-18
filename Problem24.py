# WAP to find whether the string is symmetrical or not
str = input("string: ")
mid = len(str)//2
if len(str)% 2 == 0:
    s1 = str[:mid]
    s2 = str[mid:]
else:
    s1 = str[:mid]
    s2 = str[mid+1:]

if s1 == s2:
    print("symmetrical")
else:
    print("not symmetrical")
    
