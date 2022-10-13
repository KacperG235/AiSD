from typing import Any

class Node:
    def __init__(self, data:any):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, value:any):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    def append(self, value:any):
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    def node(self, at:int):


lista = LinkedList()
lista.append(1)
lista.append(2)
print(lista.head.next.data)








