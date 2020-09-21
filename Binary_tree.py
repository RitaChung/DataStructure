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
            self.value = data

    def search(self, data):
        if data > self.value:
            if self.right:
                self.right.search()
            else:
                print("element {0} not in the tree".format(str(data)))
        elif data < self.value:
            if self.left:
                self.left.search()
            else:
                print("element {0} not in the tree".format(str(data)))
        else:
            print("element {0} is found".format(str(data)))

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

    def maxDepth(self):
        if self.value is None:
            return 0
        if self.right is None and self.left is None:
            return 1
        if self.left is None:
            return self.right.maxDepth() + 1
        if self.right is None:
            return self.left.maxDepth() + 1
        return max(self.right.maxDepth(), self.left.maxDepth()) + 1


    def minDepth(self):
        if self.value is None:
            return 0
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.minDepth() + 1
        if self.right is None:
            return self.left.minDepth() + 1
        return min(self.left.minDepth(), self.right.minDepth()) + 1

    def printGivenLevel(self, level):
        if self.value is None:
            return
        if level == 1:
            print(self.value, end=' ')
        else:
            if self.left:
                self.left.printGivenLevel(level - 1)
            if self.right:
                self.right.printGivenLevel(level - 1)


def printLevelOrder(root):
    if root.value is None:
        return
    height = root.maxDepth()
    for i in range(1, height+1):
        root.printGivenLevel(i)



root = TreeNode(12)
root.insert(6)
root.insert(14)
root.insert(3)
#print(root.PrintTree())
#print(root.maxDepth())
#print(root.minDepth())
#print(root.printGivenLevel(2))

print(printLevelOrder(root))
