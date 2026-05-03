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
