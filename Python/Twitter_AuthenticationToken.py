"""
The authentication system works by using authentication tokens. Each token has an expiry, denoted by expiryLimit. Each token expire automatically after expiryLimit minutes pass after it was last reset. When reset, the expiry time is reset to expiryLimit minutes from the time of reset.
1. A token can be reset any number of times.
2. Once a token expire it can no longer be accessed, and a reset issued to it will be ignored
3. A reset issued to a non-existent token is also ignored

Commands:
- Get command - 0 Token_id T
    generates a token token_id at time T. Only one get token per token_id is possible
- Reset command - 1 Token_id T
    resets the token token_id at time T

Note: The current Time, in the end, is the maximum time of all commands
Return the number of tokens that are active just after all commands have been executed

Example: input = [[0,1,1], [0,2,2], [1,1,5], [1,2,7]], expireLimit = 4
    return 1
"""
from collections import defaultdict

class solution:
    def AuthenticationTokens(input, expireLimit):
        dict = defaultdict()
        for comm, id, t in input:
            if comm == 0: # generate token
                if id not in dict:
                    dict[id] = t + expireLimit
                else:
                    if t > dict[id]:
                        del dict[id]
            else: # reset token
                if id in dict:
                    if t <= dict[id]:
                        dict[id] = t + expireLimit
                    else:
                        del dict[id]

        curTime = input[-1][-1]
        cnt = 0
        for id, expireTime in dict.items():
            if curTime <= expireTime:
                cnt += 1
        return cnt

    if __name__ == "__main__":
        input = [[0,1,1], [0,2,2], [1,1,5], [1,2,7]]
        print(AuthenticationTokens(input, 4))
