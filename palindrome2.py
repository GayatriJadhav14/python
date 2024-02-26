def pali(number, rev=0):
    if number == 0:
        return number == rev
    else:
        return pali(number//10,rev * 10 + number % 10) 
    
number = int(input("enter a number"))
if pali(number):
    print(f"{number}number is palindrome")
        
else:
    print(f"{number}number is not palindrome:")