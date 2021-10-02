"""
Given a typing test to a population and want to find out which key takes the longest time to press. Given the results of ta test, determine which key takes the longest to press

Input:[[0,2], [1,5], [0,9], [2,15]]

keyTimes[i][0]: ascii[a-z], a = 0, ..., z = 25
keyTimes[i][1]: time the key is pressed since the start of the test.

In the example, 'a' takes 2-0 = 2 to press, 'b' takes 5-2=3 to press.

Function description:
Complete the function slowestKey. the function must return a character, the slowest key that presses

"""
from collections import defaultdict

class solution:
    def slowestKey(keyTimes):
        dict = defaultdict()
        a_ascii = ord('a')
        prev = 0
        for c, t in keyTimes:
            if c in dict:
                dict[c] = max(dict[c], t-prev)
            else:
                dict[c] = t-prev
            prev = t
        dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)

        return chr(dict[0][0] + a_ascii)

    if __name__ == "__main__":
        keyTimes1 = [[0,2], [1,5], [0,9], [2,15]] # c
        keyTimes2 = [[0,1],[0,3],[4,5],[5,6],[4,10]] # e
        keyTimes3 = [[0,2],[1,3],[0,7]] # a
        assert slowestKey(keyTimes1)=='c', "expected: c, actual: {}".format(slowestKey(keyTimes1))
        assert slowestKey(keyTimes2)=='e', "expected: e, actual: {}".format(slowestKey(keyTimes2))
        assert slowestKey(keyTimes3)=='a', "expected: a, actual: {}".format(slowestKey(keyTimes3))
