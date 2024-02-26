#str = "Gayatri" 

str=input("Enter string")
print ("The original string  is : ",str)   
str1 = ""  
count = len(str)  
while count > 0:   
    str1 = str1+str[ count - 1 ]   
    count = count - 1 
print ("The reversed string using a while loop is : ",str1)

