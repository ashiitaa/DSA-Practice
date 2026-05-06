# FIND DIFF BETWEEN MAX AND MIN NUMBER
def find_diff(arr):
    max = float('-inf')
    min = float('inf')
    for num1 in arr:
        if num1 > max :
            max = num1
    for num2 in arr:
        if num2 < min :
            min = num2 
    for diff in arr :
        diff = max - min 

    return diff
arr = [2,4,5,6,8,1]
print('the diff between the max and min number is:', find_diff(arr))
# COUNT THE NUMBERS GREATER THAN 5
def find_count(arr):
    count = 0 
    for num in arr:
        if num > 5 :
            count = count + 1 
    return count 
arr=[1,2,4,7,9]
print ('numbers in array greater than 5 are :', find_count(arr))
# FIND THE INDEX OF FIRST EVEN NUMBER IN ARRAY
def find_even_index(arr):
    
    for i in range(len(arr)):
       
       if arr[i] % 2 == 0 :
          return i
arr = [3,5,2,7,8]
print ('index of first even number is:', find_even_index(arr))
# FIND THE FREQUENCY OF 2 IN AN ARRAY
def find_freq(arr):
    count = 0
    for num in arr:
        if num ==2 :
            count = count + 1
    return count 
arr=[3,2,5,2,7,2]
print('the frquency of 2 in an array is:', find_freq(arr))
# FIND DUPLICATE ELEMENTS IN AN ARRAY
def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
         if arr[i]==arr[j]:
           print(arr[i])

arr = [2,3,1,2,6,3,7,6]  
find_duplicate(arr)      
# FIND THE PAIRS WHOSE SUM IS 10 
def find_sum(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == 10 :
                print(arr[i] , arr[j])
arr = [2,4,6,9,1,7,8]
find_sum(arr)
