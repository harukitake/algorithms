NIL = -1
class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

n = int(input())
trees = [Node() for _ in range(n)]
