class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.first_node = None

    def traverse(self):
        if self.first_node is None:
            print("List has no element.")
        else:
            cur = self.first_node

            while cur is not None:
                print(cur.value)
                cur = cur.next

    def insert_at_start(self, data):
        newNode = Node(data)
        if self.first_node is not None:
            newNode.next = self.first_node
            self.first_node = newNode
        else:
            self.first_node = newNode

    def insert_at_end(self,data):
        newNode = Node(data)
        if self.first_node is None:
            self.first_node = newNode
        else:
            cur = self.first_node
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode

    def insert_after_item(self, x, data):
        newNode = Node(data)
        cur = self.first_node
        while cur.next is not None:
            if cur.value == x:
                break
            cur = cur.next
        if cur.value == x:
            newNode.next = cur.next
            cur.next = newNode
        else:
            print("item not in the list")

    def insert_before_item(self, x, data):
        newNode = Node(data)
        cur = self.first_node

        if self.first_node is None:
            print("item is not in list")
            return

        if self.first_node.value == x:
            newNode.next = self.first_node
            self.first_node = newNode
            return

        while cur.next is not None:
            if cur.next.value == x:
                break
            cur = cur.next

        if cur.next is None:
            print("item is not in list")
        else:
            newNode.next = cur.next
            cur.next = newNode

    def insert_at_index(self, index, data):
        newNode = Node(data)
        if index == 1:
            newNode.next = self.first_node
            self.first_node = newNode

        cur = self.first_node
        count = 1
        while cur is not None and count < index-1:
            cur = cur.next
            count += 1

        if cur is None:
            print("index out of bound")
        else:
            if cur.next is not None:
                newNode.next = cur.next
                cur.next = newNode
            else:
                cur.next = newNode

    def get_count(self):
        if self.first_node is None:
            return 0
        else:
            cur = self.first_node
            count = 1
            while cur.next is not None:
                count += 1
                cur = cur.next
            return count

    def search_item(self, x):
        if self.first_node is None:
            print('list has no element')
            return

        cur = self.first_node
        count = 1
        while cur.next is not None:
            if cur.value == x:
                print("item found")
                return True
                #return(count)
            cur = cur.next
        if cur.next is None:
            print("item is not in list")
            return False

    def delete_at_start(self):
        if self.first_node is None:
            print("the list has no element to delete")
        else:
            self.first_node = self.first_node.next

    def delete_at_end(self):
        if self.first_node is None:
            print("the list has no element to delete")
        else:
            cur = self.first_node
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None

    def delete_element_by_value(self, x):
        if self.first_node is None:
            print("the list has no element to delete")
        else:
            cur = self.first_node
            while cur.next is not None:
                if cur.next.value == x:
                    break
                cur = cur.next
            if cur.next is None:
                print('item is not in the list')
            else:
                cur.next = cur.next.next

    def reverse_linkedlist(self):
        prev = None
        cur = self.first_node
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.first_node = prev






temp = LinkedList()
temp.insert_at_start(5)
temp.insert_at_end(8)
temp.insert_after_item(8, 9)
temp.insert_before_item(9, 4)
temp.insert_at_index(5,30)
#print(temp.get_count())
#temp.search_item(4)
temp.delete_at_start()
temp.delete_at_end()
temp.traverse()
temp.delete_element_by_value(5)
temp.traverse()
temp.reverse_linkedlist()
print("--------")
temp.traverse()



