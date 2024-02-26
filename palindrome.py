#palindrome number

def pali(number):
    return str(number)==str(number)[::-1]

number=input("enter the number:")

if pali(number):
    print("number is palindrome:")
else:
    print("number is not palindrome")
