'''
You are given a List of Integers which is a list of priorities. A priority can be a number 
from 1-99. Without changing the order of the array, minimize the priority as much as
possible without changing the order.

Example:
arr = [1, 4, 8, 4] --> [1, 2, 3, 2]
'''

def changePriority(arr):
    temp = []
    # create a temp list: [[index, original prioriy]]
    for i in range(len(arr)):
        temp.append([i, arr[i]])
    # sort the temp list by priority in asc order
    temp = sorted(temp, key=lambda x: x[1])
    
    # for each item in temp list, add its new priority at the end
    # for the first priority, its new priority is 1
    temp[0].append(1)
    new_p = 1
    for i in range(1, len(temp)):
        if temp[i][1] == temp[i-1][1]:
            new_p = new_p
        else:
            new_p += 1
        temp[i].append(new_p)
    
    # resort the temp list by index 
    temp = sorted(temp, key=lambda x:x[0])
    print(temp)
    new_arr = []
    
    for i in range(len(temp)):
        new_arr.append(temp[i][2])
    return new_arr
    
    
arr = [1, 4, 8, 4]
print(changePriority(arr))