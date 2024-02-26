'''year = int(input("Enter a year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is a not leap year")
    else:
        print(year,"is a leap year")
        
else:
    print(year, "is not a leap year")'''
    
    
    
    
    #second way

def leap(year):
    if(year%4==0 and year %100 != 0) or (year % 400 == 0):
    
        return True
    else:
        return False
    
year = int(input("Enter a year:"))

if leap(year):
    print(year, "is a leap year")
else:
    print(year,"is not leap year")


            