import os
os.system ('cls')


# class node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# class single circular linked list 
class circularlinkedlist:
    def __init__(self):
        self.head = None
    
    # menambahkan data
    def add_data(self,data):
        newNode = Node(data)
        temp = self.head
        newNode.next = self.head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newNode
        else:
            newNode.next = newNode
        self.head = newNode
                
    def print(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print( str (temp.data) +' -> '+ str (temp.next.data))
                temp = temp.next
                if temp == self.head:
                    break
                
                
list = circularlinkedlist()
list.add_data(1) 
list.add_data(2) 
list.add_data(3) 
list.add_data(4)
list.add_data(5)
list.add_data(6)
list.add_data(7)
list.add_data(8)
list.add_data(9)
list.add_data(10)
print("isi list : ")
list.print()


    
 