class stack(object):
    def __init__(self):
        self.seq = []

    def push(self, val):
        self.seq.append(val)
        print("add element {0} into stack".format(str(val)))

    def peek(self):
        return self.seq[-1]

    def pop(self):
        if len(self.seq) <= 0:
            print("there is no element in stack")
        else:
            val = self.seq.pop()
            print("remove the top element {0}".format(str(val)))

    def traverse(self):
        return self.seq


AStack = stack()
AStack.push("Mon")
AStack.push("Tue")
AStack.push("Tue")
print(AStack.traverse())
AStack.pop()
AStack.push("Wed")
AStack.push("Thu")
print(AStack.peek())
print(AStack.traverse())
