"""
Given an arrary of integers. Find the min moves required to swap numbers such that all even numbers show in the first part of the array and follow with all odd numbers

example:
arr = [8, 5, 11, 4, 6] return 2
explanation: first swap 5 and 6, and second swap 11, 4

"""
def MinSwap(arr):
    i, j = 0, len(arr)-1
    cnt = 0
    while i < j :
        # left = even, right = odd, move forward
        print("i = {}({}), j = {}({})".format(arr[i], i, arr[j], j))
        if arr[i] % 2 == 1 and arr[j] % 2 == 0:
            cnt += 1
            i += 1
            j -= 1
            print("swap + 1 = {}".format(cnt))
        # left = even, right =
        elif arr[i] % 2 == 0:
            i += 1
        elif arr[j] % 2 == 1:
            j -= 1

    return cnt

if __name__ == "__main__":
    arr = [8, 5, 11, 4, 6]
    arr1 = [1,3,5,7,6,8,12,9]
    arr2 = [ 1, 3, 2, 4, 7, 6, 9, 10 ]
    # assert MinSwap(arr) == 2
    print(MinSwap(arr2))
