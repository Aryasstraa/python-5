import os
os.system ('cls')

class Node:
    def __init__(self, data = None):
        self.data = data
        self.previous = self
        self.next = self

class DCLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
     
    def __repr__(self):
        string = ""
          
        if(self.head == None):
            string += "Double Circular Linked List Kosong"
            return string
          
        string += f"Double Circular Linked List:\n Data : {self.head.data}, Next : {self.head.next.data}, Prev : {self.head.previous.data}\n"      
        temp = self.head.next
        while(temp != self.head):
            string += f" Data : {temp.data}, Next : {temp.next.data}, Prev : {temp.previous.data}\n"
            temp = temp.next
        return string
     
    def append(self, data):
        self.insert(data, self.count)
        return
     
    def insert(self, data, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"index melebihi batas: {index}, size: {self.count}")
         
        if self.head == None:
            self.head = Node(data)
            self.count = 1
            return
         
        temp = self.head
        if(index == 0):
            temp = temp.previous
        else:
            for _ in range(index - 1):
                temp = temp.next
         
        temp.next.previous = Node(data)
        temp.next.previous.next, temp.next.previous.previous = temp.next, temp
        temp.next = temp.next.previous
        if(index == 0):
            self.head = self.head.previous
        self.count += 1
        return
     
    def remove(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"index melebihi batas: {index}, size: {self.count}")
             
        if self.count == 1:
            self.head = None
            self.count = 0
            return
         
        target = self.head
        for _ in range(index):
            target = target.next
             
        if target is self.head:
            self.head = self.head.next
             
        target.previous.next, target.next.previous = target.next, target.previous
        self.count -= 1
         
    def index(self, data):
        temp = self.head
        for i in range(self.count):
            if(temp.data == data):
                return i
            temp = temp.next
        return None
     
    def get(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index melebihi batas: {index}, size: {self.count}")
             
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.data
     
    def size(self):
        return self.count
     
    def display(self):
        print(self)
    
    def searchList(self, value):
        position = 0
        found = 0
        if self.head is None:
            print("Tidak ada data pada linked list")
        else:
            temp_node = self.head
            while temp_node:
                position = position + 1
                if temp_node.data == value:
                    print("Data berada pada index ke: " + str(position-1) + " atau posisi ke " + str(position))
                    found = 1
                    break
                if temp_node == self.tail:
                    print("Data tidak ditemukan pada list")
                    break
                temp_node = temp_node.next

    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("Menu\n1. Append\n2. Insert\n3. Remove\n4. Get\n5. Size\n6. Display\n7. Search")
            pilihan=str(input(("Silakan masukan pilihan anda:")))
            if(pilihan=="1"):
                obj = int(input("Masukan data yang ingin anda tambahkan: "))
                self.append(obj)
            elif(pilihan=="2"):
                obj = int(input("Masukan data yang ingin anda tambahkan: "))
                inx = int(input("Pada index ke: "))
                self.insert(obj,inx)
            elif(pilihan=="3"):
                inx = int(input("Masukkan index: "))
                self.remove(inx)
            elif(pilihan=="4"):
                inx = int(input("Masukkan index : "))
                print(self.get(inx))
            elif(pilihan=="5"):
                print(self.size())
            elif(pilihan=="6"):
                self.display()
            elif(pilihan=="7"):
                obj = int(input("Data yang ingin dicari: "))
                self.searchList(obj)
            else:
                pilih="n"

if __name__ == "__main__":
# execute only if run as a script
    l = DCLL()
    l.mainmenu()