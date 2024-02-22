#using for loop

'''def reverse(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1

str="Gayatri"
print("the original string is:",str)
print("the reverse string is",reverse(str))'''

#user input

'''def reverse(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1

a=input("Enter the string:")
print("The original string is:",a)
print("the reverse string is",reverse(a))'''

#using while loop

'''def reverse(str):
    str1=""
    count = len(str)
    while count>0:
        str1 +=a [count-1]
        count = count -1
    a=input("ENter the string:")
    print("The original string is:",a)
    print("the reverse string is ",str1)'''
    
#str = "Gayatri" 
'''
str=input("Enter string")
print ("The original string  is : ",str)   
str1 = ""  
count = len(str)  
while count > 0:   
    str1 = str1+str[ count - 1 ]   
    count = count - 1 
print ("The reversed string using a while loop is : ",str1)

'''

'''
#using slice
def rev(str):
    return str[::-1]
a=input("enter name")
print("the original string:",a)
print("the reverse string:",rev(a))
'''

#using recursive function

'''def rev(str):
    if len(str)==0:
        return str
    else:
        return rev(str[1:]) + str[0]
    
a=input("enter name")
print("the original string:",a)
print("the reverse string:",rev(a))'''


 
 
 
def rev(s):
    s_list = list(s)
    start = 0
    end = len(s) - 1
    while start < end:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
    return ''.join(s_list)   
a=input("enter name")
print("the original string:",a)
print("the reverse string:",rev(a))


