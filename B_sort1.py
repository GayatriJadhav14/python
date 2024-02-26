#using temp variable

def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                
arr=list(map(int,input("Enter the array").split()))
sort(arr)
print("bubble sorted array is: ",arr)