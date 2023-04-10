import os
os.system ('cls')

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self.head.prev = self.tail

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.tail.next = self.head
        self.head.prev = self.tail

    def delete_node(self, key):
        if self.is_empty():
            return

        cur_node = self.head
        if cur_node.data == key:
            # delete the only node in the list
            if cur_node.next == self.head:
                self.head = None
                self.tail = None
            else:
                self.head = cur_node.next
                self.head.prev = self.tail
                self.tail.next = self.head
            return

        while cur_node.next != self.head:
            if cur_node.data == key:
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev
                return
            cur_node = cur_node.next

        # check the last node in the list
        if cur_node.data == key:
            cur_node.prev.next = self.head
            self.head.prev = cur_node.prev
            self.tail = cur_node.prev

    def display(self):
        if self.is_empty():
            print("List is empty")
            return

        cur_node = self.head
        print("List nodes:")
        while cur_node.next != self.head:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print(cur_node.data)
        
dllist = DoubleCircularLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.append(6)
dllist.append(7)
dllist.append(8)
dllist.append(9)
dllist.append(10)
dllist.prepend(0)
dllist.prepend(1)
dllist.prepend(2)
dllist.prepend(3)
dllist.prepend(4)
dllist.prepend(5)
dllist.prepend(6)
dllist.prepend(7)
dllist.prepend(8)
dllist.prepend(9)
dllist.prepend(10)
dllist.display()
dllist.delete_node(1)
dllist.display()