"""
Given two string list, a and b, return the minimum characters change required
to make a[i] an anagram of b[i]. Return -1 if the len(a[i]) != len(b[i])

Example:
a = ["tea", "tea", "ape"], b = ["toe", "tae", "apes"]
return = [1, 0, -1]
"""
def findMinChange(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] not in b:
            cnt += 1

    return cnt
def minChange(a, b):
    n = len(a)
    res = [0] * n
    for i in range(n):
        if len(a[i]) != len(b[i]):
            res[i] = -1
        else:
            res[i] = findMinChange(a[i], b[i])
    return res
if __name__ == "__main__":
    a = ["tea", "tea", "ape"]
    b = ["toe", "tae", "apes"]
    print(minChange(a, b))
