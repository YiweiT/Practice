'''
1. sort both arrays by their values
2. set left and right pointers, left = 0 for a_sorted and right = len(b_sorted)-1 for b_sorted
3. start the while loop:
    calucate the current sum
    compare
'''
def solution(a, b, target):
    temp_v = float('-inf')
    a_sorted = sorted(a, key=lambda x: x[1])
    b_sorted = sorted(b, key=lambda x: x[1])
    left = 0
    right = len(b_sorted) - 1
    res = []
    
    while left < len(a_sorted) and right >= 0:
        sum = a_sorted[left][1] + b_sorted[right][1]
        
        if sum > target:
            right -= 1
        else:
            if temp_v <= sum:
                if temp_v < sum:
                    res = []
                    temp_v = sum
                res.append([a_sorted[left][0], b_sorted[right][0]])
                cnt = right
                
                while cnt > 0 and b_sorted[cnt][1] == b_sorted[cnt-1][1]:
                    res.append([a_sorted[lcnt][0], b_sorted[cnt-1][0]])
                    cnt -= 1
            left += 1
    
    if not res:
        res = [[]]
    return res

if __name__ == "__main__":
    a = [[1, 2], [2, 4], [3, 6]]
    b = [[1, 2]]
    target = 7  
    res = solution(a, b, target)
    print(res)