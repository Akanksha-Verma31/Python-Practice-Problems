# WAP to validate Email id given by user
import string
str1=("muteen@gmail.com")
str2=("mateen@gmail.com")
if (str1[0:8])==(str2[0:8]):
    print("valid mail")
else:
    print("invalid mail")
