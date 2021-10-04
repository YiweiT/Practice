"""
Given a array of (parent, child) pairs, determine whether it could be a binary tree.
E1: More than 2 children
E2: Duplicate Edges
E3: Cycle
E4: Multiple Roots
E5: Any other error
else: print out the tree in the format of (parent(child)(child))
"""
from collections import defaultdict

def convert2Tree(input):
    parent_d = defaultdict()
    child_d = defaultdict()
    nodes = set()
    for p, c in input:
        nodes.add(p)
        nodes.add(c)
        if p in parent_d:
            if c not in parent_d[p]:
                parent_d[p].append(c)
                if len(parent_d[p]) > 2:
                    return 'E1: More than 2 children'
            else:
                return "E2: Duplicate Edges"

        else:
            parent_d[p] = [c]

        if c in child_d and child_d[c] != p:
            return "E3: Cycle"

        else:
            child_d[c] = p
    # sort parent_d's values
    for p in parent_d:
        parent_d[p].sort(reverse=True)
    # find the root of the tree
    # root should not be a child, so it will not be present in child_d dictionary's key set
    root = ""
    for node in nodes:
        if node not in child_d:
            root = node
    if root == "":
        return "E3: Cycle"
    res = ""
    stack = [(root, 0)]
    visited = []
    prev_level = 0
    while stack:
        p, level = stack.pop()
        visited.append(p)

        if level < prev_level:
            for i in range(level, prev_level):
                res += ')'
            prev_level = level
        res += '(' + p
        if p in parent_d:

            for c in parent_d[p]:

                stack.append((c, level+1))
        else:
            # p is a child
            res += ')'
            prev_level = level

    for i in range(prev_level):
        res += ')'
    if len(visited) < len(nodes):
        return "E4: Multiple Roots"
    return res

if __name__ == "__main__":
    graph = [('a', 'b'), ('b', 'c')] # print out (a(b(c)))
    graph1 = [('a', 'b'), ('b', 'c'), ('c', 'a')] # print cycle
    graph2 = [('a', 'b'), ('b', 'c'), ('b', 'd'), ('a','e'), ('d', 'e')] # double parent
    graph3 = [('a', 'b'), ('b', 'c'), ('b', 'd'), ('d','e'), ('d', 'f'), ('d', 'g')] # triple children
    graph4 = [('b', 'c'), ('a', 'b'), ('b', 'd'), ('d','e'), ('d', 'f'), ('c','h'), ('c', 'i')] # (a(b(c)(d(e)(f))))
    graph5 = [('b', 'd'), ('d', 'e'), ('a', 'b'), ('a', 'c'), ('c', 'f'), ('e', 'g')] # (a(b(d(e(g))))(c(f)))


    print(convert2Tree(graph5))
