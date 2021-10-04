"""
Given a array of (parent, child) pairs, determine whether it could be a binary tree.
1. Print out "Cycle" if there is a Cycle
2  If children greater than 2 -> "children > 2"
3. If a child has more than one parent -> "parents > 1"
4. repeated edge -> "repeated edge"
else: print out the tree in the format of (parent(child)(child))
"""
from collections import defaultdict

def convert2Tree(input):
    parent_d = defaultdict()
    child_d = defaultdict()
    for p, c in input:
        if p in parent_d:
            if c not in parent_d[p]:
                parent_d[p].append(c)
                if len(parent_d[p]) > 2:
                    print('Children > 2')
                    return
            else:
                print("Repeat edge")
                return
        else:
            parent_d[p] = [c]

        if c in child_d and child_d[c] != p:
            print("parents > 1")
            return
        else:
            child_d[c] = p
    stack = [(graph[0][0], 0)]
    for p in parent_d:
        parent_d[p].sort(reverse=True)
    res = ""
    visited = []
    prev_level = 0
    while stack:
        p, level = stack.pop()
        visited.append(p)

        if level < prev_level:
            res += ')'
        res += '(' + p
        if p in parent_d:

            for c in parent_d[p]:
                if c in visited:
                    print('Cycle')
                    return
                stack.append((c, level+1))
        else:
            # p is a child
            res += ')'
            prev_level = level

    for i in range(prev_level):
        res += ')'
    print(res)

if __name__ == "__main__":
    graph = [('a', 'b'), ('b', 'c')] # print out (a(b(c)))
    graph1 = [('a', 'b'), ('b', 'c'), ('c', 'a')] # print cycle
    graph2 = [('a', 'b'), ('b', 'c'), ('b', 'd'), ('a','e'), ('d', 'e')] # double parent
    graph3 = [('a', 'b'), ('b', 'c'), ('b', 'd'), ('d','e'), ('d', 'f'), ('d', 'g')] # triple children
    graph4 = [('b', 'c'), ('a', 'b'), ('b', 'd'), ('d','e'), ('d', 'f'), ('c','h'), ('c', 'i')] # (a(b(c)(d(e)(f))))

    convert2Tree(graph4)
