'''
Given an array of integers, you need to find the number of ways to split the array into two 
subarrays and the sum of left subarray is strickly greater than that of the right subarray
and neither of subarrays can be empty

example: array: [10, 4, -8, 7] --> 2
[10] and [4, -8, 7]: left = 10 > 3 = right
[10, 4] and [-8, 7]: left = 14 > -1 = right
[10, 4, -8] and [7]: left = 6 < 7 = right (do not count)
'''

def splipArray(arr):
    left = sum(arr)
    right = 0
    cnt = 0
    for i in range(len(arr)-1, -1, -1):
        left -= arr[i]
        right += arr[i]
        if left > right:
            cnt += 1
    return cnt

arr = [10, 4, -8, 7]
print(splipArray(arr))