string1=input("enter a string")
string2=input("enter 2nd string")
print(len(string1))
print(len(string2))
print(string1[::-1])
print(string2[::-1])
if string1==string2:
    print("Both are equal")
else:
    print("Both are not equal")
if string1==string1[::-1]:
    print("The string is a palindrome")
else:
    print("String is not a palindrome")
if string1 in string2:
    print("substring is present")
else:
    print("substring is not present")
