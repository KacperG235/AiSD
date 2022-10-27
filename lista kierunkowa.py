from typing import Any


class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: any) -> None:
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        self.tail = self.head

    def append(self, value: any) -> None:
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            self.tail = new

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
        if self.head.next == None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            lastNode = temp.next
            temp.next = None
            lastNode = None

    def remove(self, after: Node) -> Any:
        temp = self.head
        if temp is not None:
            if temp.data == after:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == after:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def print(self) -> None:
        temp = self.head
        while temp:
            print(temp.data, "-> ", sep=' ', end='', flush=True)
            temp = temp.next

    def len(self) -> int:
        temp = self.head
        i = 0
        while temp:
            i += 1
            temp = temp.next
        return i


class Stack:
    def __init__(self):
        self.head = None

    def push(self, element: any) -> None:
        if self.head == None:
            self.head = Node(element)
        else:
            newnode = Node(element)
            newnode.next = self.head
            self.head = newnode

    def pop(self) -> float:
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

    def print(self) -> None:
        temp = self.head
        print('')
        while temp:
            print(temp.data)
            temp = temp.next

    def len(self) -> int:
        temp = self.head
        i = 0
        while temp:
            i += 1
            temp = temp.next
        return i


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def peek(self):
        return self.front.data

    def enqueue(self, element: any) -> None:
        temp = Node(element)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self) -> None:
        if self.front == None:
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None

    def print(self) -> None:
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next

    def len(self) -> int:
        temp = self.front
        i = 0
        while temp:
            i += 1
            temp = temp.next
        return i


def main():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.append(33)
    ll.print()


if __name__ == "__main__":
    main()
