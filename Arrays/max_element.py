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
