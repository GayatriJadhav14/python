#using recursive function

def rev(str):
    if len(str)==0:
        return str
    else:
        return rev(str[1:]) + str[0]
    
a=input("enter name")
print("the original string:",a)
print("the reverse string:",rev(a))

