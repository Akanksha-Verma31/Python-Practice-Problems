# Check whether the character entered by user is vowel or consonent.

# using membership operator
ch = input("Enter a character: ")
vowel = "aeiouAEIOU"
if ch in vowel:
    print("vowel")
else:
    print("consonent")
    
    
# using list
x=input("enter a character:")
vowel=['a','e','i','o','u','A','E','I','O','U']
if x in vowel:
print(x," is a vowel")
else:
print(x," is a consonant")

# using logical operator
x=int(input("Enter character"))
x = input("Enter Character : ")

if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A'
or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
print(x, "is a Vowel")
else:
print(x, "is a Consonant")
