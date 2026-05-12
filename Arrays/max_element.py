def find_max(arr):
  max_element = arr[0]

  for num in arr:
    if num > max_element:
      max_element = num
   return max_element 

arr = [3,5,7,8,2]
print('maximum element is:',
find_max(arr))
#time complexity : 0(n)
# space complexity : 0(1)
# MOVE ALL ZERO TO THE END OF ARRAY
def move_zero(arr):
    new_arr = []
    zero = 0 

    for num in arr:

        if num != 0:
          new_arr.append(num)
        else :
           zero = zero + 1 

    for i in range(zero):
       
       new_arr.append(0)

    return new_arr

arr = [3,0,0,8,5,0,2]
print('new array is:', move_zero(arr))
