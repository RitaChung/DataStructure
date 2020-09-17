class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.value:
                if self.right is None:
                    self.right = Node(data)
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



root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.PrintTree())


def findval(self, lkpval):
    if lkpval < self.data:
        if self.left is None:
            return str(lkpval) + " Not Found"
        return self.left.findval(lkpval)
    elif lkpval > self.data:
        if self.right is None:
            return str(lkpval) + " Not Found"
        return self.right.findval(lkpval)
    else:
        print(str(self.data) + ' is found')
        
#https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
