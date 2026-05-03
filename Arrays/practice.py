# COUNT EVEN NUMBERS
def count_even(arr):
  count = 0
  for num in arr:
   if  num % 2 == 0:
     count = count + 1 

  return count  

arr = [3,4,8,6,9]

print ('even num are:', count_even(arr))

# FIND SUM OF ARRAY
def find_sum(arr):
  total = 0

for num in arr :
  total = total + num 
return total 

arr = [3,5,6,7,1]

print = ('the sum is:', find_sum(arr))
# COUNT POSITIVE NUMBERS
def count_positive(arr):
    count = 0 
    for num in arr:
        if num > 0 :
           count = count + 1
      
    return count  

arr = [2,-6,-3,4,-9]

print('total positive numbers are:', count_positive(arr))
# SMALLEST ODD NUMBER
def find_smallest_odd(arr):
    odd = float('inf')

    for num in arr:
        if num % 2 == 1 and num < odd :
            odd = num 

    return odd
 
arr = [2,3,5,9,4]

print ('the smallest odd number is:', find_smallest_odd(arr))
# largest even number
def largest_even_no(arr):
    largest = float('-inf')
    
    for num in arr:
        if num > largest and num % 2 == 0 :
            largest = num 
            return num 
        
arr = [3,6,2,1,4]
print ('the largest number is:', largest_even_no(arr))



