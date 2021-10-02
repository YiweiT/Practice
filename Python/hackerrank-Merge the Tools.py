def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i < len(string):
        coll = ''
        for j in range(i, i+k):
            # print('string[{}]:{}'.format(j, string[j]))
            if string[j] not in coll:
                
                coll += string[j]
        print(coll)
        i += k
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)