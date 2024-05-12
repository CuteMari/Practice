
class Node:
    def __init__(self, item):
        self.key = item
        self.p = None
        self.left = None
        self.right = None
    
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
    
    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return max(leftDepth, rightDepth) + 1
    

class BinaryTree:
    def __init__(self,r):
        self.root = r
    
    def size(self):
        if self.root: return self.root.size()
        else: return 0
    
    def depth(self):
        if self.root: return self.root.depth()
        else: return 0


# 전위 순회
def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)
    
# 탐색 함수
def tree_search(x,k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    
    return x

# 최솟값 함수
def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x

# 최댓값 함수
def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x

# 직후 노드 함수
def tree_successor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y

# 직전 노드 함수
def tree_predecessor(x):
    if x.left != None:
        return tree_maximum(x.left)
    y = x.p
    while y != None and x == y.left:
        x = y
        y = y.p
    return y

# 삽입 연산 함수
def tree_insert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

# 노드 옮기는 함수
def transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p

# 삭제 연산 함수
def tree_delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y


###################################
n1 = Node(15)
n2 = Node(6)
n3 = Node(18)
n4 = Node(7)
n5 = Node(17)
BT = BinaryTree(n1)

n1.left = n2
n2.p = n1
n1.right = n3
n3.p = n1
n2.right = n4
n4.p = n2
n3.left = n5
n5.p = n3

n6 = Node(20)
tree_insert(BT, n6)
