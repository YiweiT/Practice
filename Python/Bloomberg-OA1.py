
# Two destinations: New York (ny) and San Fransisco (sfo)
# for each engineer, there are two cost to flight to the destinations, respectively
# Task: find the min cost of sending engineers to destination
# Limitation: half to ny and half to sfo

# Param: ny: List[int], sfo: List[int]
#  (length of both lists are the same)
#  (length could be odd)

def minFlightCost(ny: List[int], sfo: List[int]) -> int:
    if not ny and not sfo: return 0
    diff = {} # (index, ny cost - sfo cost)
    n = len(ny)
    # suppose first we send all engineers to ny
    ny_all = sum(ny)
    # for those whose cost to sfo is less then cost to ny, we will send to sfo
    for i in range(n):
        diff[i] = ny[i] - sfo[i]
    # sort the diff by diff btw ny[i] and sfo[i]
    print(diff)
    diff = sorted(diff.items(), key=lambda x: x[1])
    print('sorted diff: {}'.format(diff))
    mid = n // 2
    sfo_half = sum([sfo[i] for i in range(mid+1)])
    # and the odd case
    if n % 2 == 1 and diff[mid+1] > 0:
        ny_all -= diff[mid+1]
    
    return ny_all - sfo_half

ny = [100, 200, 300, 400, 500, 600]
sfo = [800, 700 ,500 ,100 ,600 ,400]

minFlightCost(ny, sfo)