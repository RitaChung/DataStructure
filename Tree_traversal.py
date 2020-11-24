# in-order traversal - the left subtree is visited first, then the root and later the right sub-tree
# pre-order traversal - the root node is visited first, then the left subtree and finally the right subtree
# post-order traversal - the root node is visited last.
#   first, traverse the left subtree, than the right subtree and finally the root node

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.value = TreeNode(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()

    #in-order traversal: left -> root -> right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.value)
            res = res + self.inorderTraversal(root.right)
        return res

    #pre-order traversal: root -> left -> right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.value)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    #post-order traversal: left -> right -> root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.value)
        return res

root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))
