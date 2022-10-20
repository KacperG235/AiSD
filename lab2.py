from typing import Any

class Node:
    def __init__(self, data:any) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value:any) -> None:
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def append(self, value:any) -> None:
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def node(self, at: int) -> Node:
        if at == 1:
            return self.head.data
        i = 1
        temp = self.head
        while temp.next:
            temp = temp.next
            i += 1
            if i == at:
                break
        if i == at:
            return temp.data
        else:
            print("Error")

    def insert(self, value: any, after: Node) -> None:
        temp = Node(value)
        temp.next = after.next
        after.next = temp

    def pop(self) -> any:
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def remove_last(self) -> any:
        temp = self.head
        while self.head:
            temp = temp.next
        tmp = temp.next
        ostatnia = temp.next
        temp.next = None
        lastNode = None
        return tpm.data



def main():
    lista = LinkedList()
    lista.append(6)
    lista.push(7)
    lista.push(1)
    lista.append(4)
    lista.insert(8, lista.head.next)
    lista.remove_last()
    print(lista.node(4))


if __name__ == "__main__":
    main()
