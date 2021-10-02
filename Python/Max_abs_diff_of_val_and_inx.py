"""
Given an unsorted array A of N integers, A_{1}, A_{2}, ...., A_{N}.      Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) or absolute difference of two elements of an array A is defined as |A[i] – A[j]| + |i – j|, where |A| denotes
the absolute value of A.
"""

class Solution:
    def maxDistance(nums):
        max1 = max2 = float("-inf")
        min1 = min2 = float("inf")

        for i in range(len(nums)):
            max1 = max(max1, nums[i] + i)
            min1 = min(min1, nums[i] + i)
            max2 = max(max2, nums[i] - i)
            min2 = min(min2, nums[i] - i)
        return max(max1 - min1, max2 - min2)

    if __name__ == "__main__":
        nums = [-70, -64, -6, -56, 64,61, -57, 16, 48, -98]
        print(maxDistance(nums))
