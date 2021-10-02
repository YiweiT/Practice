def gap(a,b):
    return abs(ord(a)-ord(b))

def func(s,k):
    temp,longest= '', ''
    for i in range(0, len(s)-1):
        print(temp)
        temp += s[i]
        if gap(temp[-1], s[i+1]) > k:
            print(gap(temp[-1], s[i+1]), 'test for longest')
            longest = longest if len(longest) > len(temp) else temp

            temp = ''
        print(longest, temp)
        print('----------------')
    print('final temp:', temp, 'final longest:', longest)
    if longest == '':
        longest = temp + s[-1]
    return longest

print('apple, 25:', func('apple', 25))
print('apple, 0:',func('apple', 0))
