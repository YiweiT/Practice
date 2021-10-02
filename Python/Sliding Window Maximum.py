'''
Sliding window maximum
Given an array of integer, nums and an integer, k, represents the size of sliding window
return an array which contains tha maximum integer for every window

example:
array = [1, 3 , -1, -3, 5, 3, 6, 7], k = 3
output = [3, 3, 5, 5, 6, 7]
sliding window                 max
----------------------------------
[1, 3, -1] -3, 5, 3, 6, 7       3
1, [3, -1. -3] 5, 3, 6, 7       3
1, 3, [-1, -3, 5] 3, 6, 7       5
1, 3, -1, [-3, 5, 3] 6, 7       5
1, 3, -1, -3, [5, 3, 6] 7       6
1, 3, -1, -3, 5, [3, 6, 7]      7

'''
def solution(arr k):
    output = []
    q = collections.deque() # monotic deque (alsway decreasing) store index
    l = r = 0

    while r < len(arr):
        # pop the last item if nums[q[-1]] < nums[r]
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # check wether left pointer is out of bound
        if l > q[0]:
            q.popleft()
        
        if r - l + 1 >= k:
            output.append(nums[q[]])