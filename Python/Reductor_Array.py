"""
Given two integer arrays a and b, and an integer value d, your task is to find the comparator value between these arrays.

The comparator value is defined as the number of elements x ∈ a such that there are no elements y ∈ b where |x - y| ≤ d. In other words, it's the number of elements in a that are more than d away from any element of b.

Return the comparator value as an integer.

For eg. a = [2, 9] and b = [16, 13, 8], d = 3 should return 1.

n = 9
9 - 16 = 7 > 3
9 - 13 = 4 > 3
9 - 8 = 1 < 3

n = 2 comparator
2 - 16 = 14 > 3
2 - 13 = 11 > 3
2 - 8 = 6 > 3
"""
def countComparator(a, b, k):
    cnt = 0
    for i in range(len(a)):
        curNo = 0
        for j in range(len(b)):
            if abs(a[i] - b[j]) >= k:
                curNo += 1
        if curNo == len(b):
            cnt += 1
    return cnt

if __name__ == "__main__":
    a = [2, 9]
    b =  [16, 13, 8]
    k = 3
    print(countComparator(a, b, k))
