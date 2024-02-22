import array as arr    
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])    
     
# changing first element 1 by the value 0.  
numbers[0] = 0       
print(numbers)          # Output: array('i', [0, 2, 3, 5, 7, 10])  
  
# changing last element 10 by the value 8.  
numbers[5] = 8      
print(numbers)          # Output: array('i', [0, 2, 3, 5, 7, 10])      
     
# replace the value of 3rd to 5th element by 4, 6 and 8  
numbers[2:5] = arr.array('i', [4, 6, 8])      
print(numbers)          # Output: array('i', [0, 2, 4, 6, 8, 10])    