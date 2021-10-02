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
        print(dict, dict[0][0], ord('a'))
        return chr(dict[0][0] + a_ascii)

    if __name__ == "__main__":
        keyTimes1 = [[0,2], [1,5], [0,9], [2,15]] # c
        keyTimes2 = [[0,1],[0,3],[4,5],[5,6],[4,10]] # e
        keyTimes3 = [[0,2],[1,3],[0,7]] # a
        print(slowestKey(keyTimes1))
        print(slowestKey(keyTimes2))
        print(slowestKey(keyTimes3))
