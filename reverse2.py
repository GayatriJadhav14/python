#user input

def reverse(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1

a=input("Enter the string:")
print("The original string is:",a)
print("the reverse string is",reverse(a))