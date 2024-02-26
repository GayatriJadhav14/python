def pali(number):
    
    temp = number
    reverse = 0
    while temp > 0:
        digit = temp % 10
        reverse = reverse*10+digit
        temp//=10
        
    return number == reverse
    
number = int(input("enter the number"))
if pali(number):
    print("number is palidrome:")
else:
    print("number is not palidrome:")

    
        
    