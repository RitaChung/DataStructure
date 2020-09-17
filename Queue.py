class queue(object):
    def __init__(self):
        self.queue = []

    def insert(self, val):
        self.queue.insert(0,val)
        print("add element {0} into queue".format(str(val)))

    def pop(self):
        if len(self.queue) > 0:
            val = self.queue.pop()
            print("remove element {0} from queue".format(str(val)))
        else:
            print("no element in the queue")

    def size(self):
        return len(self.queue)

    def traverse(self):
        return self.queue


AQueue = queue()
AQueue.insert("Sun")
AQueue.insert("Mon")
AQueue.insert("Tue")
print(AQueue.size())
AQueue.pop()
print(AQueue.traverse())
