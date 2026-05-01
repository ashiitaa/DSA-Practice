def find_sec_max(arr):

    first_max = float('-inf')
    sec_max = float('-inf')

    for num in arr:

        if num > first_max:
            sec_max = first_max
            first_max = num

        elif num > sec_max and num != first_max:
            sec_max = num

    return sec_max


arr = [2,6,7,9,1]

print("sec largest number is:", find_sec_max(arr))
