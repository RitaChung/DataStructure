class Node(object):
    def __init__(self, prev=None, value=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

class Doubly_LinkedList(object):
    def __init__(self):
        self.first_node = None

    def traverse(self):
        if self.first_node is None:
            print("there is no element in the list")
        else:
            cur = self.first_node
            while cur.next is not None:
                print(cur.value)
                cur = cur.next
            print(cur.value)
            print("reverse")
            while cur is not None:
                print(cur.value)
                cur = cur.prev

    def insert_at_first(self, x):
        newNode= Node(value=x)
        if self.first_node is None:
            self.first_node = newNode
        else:
            self.first_node.prev = newNode
            newNode.next = self.first_node
            self.first_node = newNode


    def insert_at_end(self, x):
        newNode = Node(value=x)
        if self.first_node is None:
            self.first_node = newNode
        else:
            cur = self.first_node
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur

    def insert_after_item(self,x,data):
        newNode = Node(value=data)
        if self.first_node is None:
            print("item is not in the list")
            return
        else:
            cur = self.first_node
            while cur is not None:
                if cur.value == x:
                    break
                cur = cur.next
            if cur is None:
                print("item is not in the list")
            else:
                cur.next.prev = newNode
                newNode.prev = cur
                newNode.next = cur.next
                cur.next = newNode

    def insert_before_item(self,x,data):
        newNode = Node(value=data)
        if self.first_node is None:
            print("item is not in the list")
            return
        else:
            cur = self.first_node
            while cur is not None:
                if cur.value == x:
                    break
                cur = cur.next
            if cur is None:
                print("item is not in the list")
            else:
                cur.prev.next = newNode
                newNode.prev = cur.prev
                newNode.next = cur
                cur.prev = newNode

    def delete_at_start(self):
        if self.first_node is None:
            print("there is no element in the list")
            return
        else:
            cur_next = self.first_node.next
            self.first_node = cur_next
            self.first_node.prev = None

    def delete_at_end(self):
        if self.first_node is None:
            print("there is no element in the list")
            return
        else:
            cur = self.first_node
            while cur.next is not None:
                cur = cur.next
        cur.prev.next = None

    def delete_element_by_value(self, x):
        if self.first_node is None:
            print("there is no element in the list")
        else:
            cur = self.first_node
            while cur is not None:
                if cur.value == x:
                    break
                cur = cur.next
            if cur is None:
                print("item is not in the list")
            else:
                if cur.prev is not None:
                    cur.prev.next = cur.next
                if cur.next is not None:
                    cur.next.prev = cur.prev




# 5, 9, 3, 8
temp = Doubly_LinkedList()
temp.insert_at_first(3)
temp.insert_at_first(5)
temp.insert_at_end(8)
temp.insert_after_item(5,9)
temp.insert_before_item(8,10)
temp.delete_at_start()
temp.delete_at_end()
temp.insert_at_first(11)
temp.insert_at_first(14) # 14, 11, 9, 3, 10
temp.delete_element_by_value(11)
temp.traverse()