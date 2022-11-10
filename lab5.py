from typing import Any, Callable


COUNT = [10]


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        return str(self.value)

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any) -> None:
        temp = BinaryNode(value)
        self.left_child = temp

    def add_right_child(self, value: Any) -> None:
        temp = BinaryNode(value)
        self.right_child = temp

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()
        print(self.value)
        if self.right_child is not None:
            self.right_child.traverse_in_order()

    def traverse_post_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()
        if self.right_child is not None:
            self.right_child.traverse_in_order()
        print(self.value)

    def traverse_pre_order(self):
        print(self.value)
        if self.left_child is not None:
            self.left_child.traverse_in_order()
        if self.right_child is not None:
            self.right_child.traverse_in_order()


class BinaryTree:
    root: 'BinaryNode'

    def __init__(self, root=None):
        self.root = root

    def traverse_in_order(self):
        self.root.traverse_in_order()

    def traverse_post_order(self):
        self.root.traverse_post_order()

    def traverse_pre_order(self):
        self.root.traverse_pre_order()


def main():
    test1 = BinaryNode(1)
    test2 = BinaryNode(37)
    node = BinaryNode('notak', test1, test2)
    drzewo = BinaryTree(node)
    drzewo.traverse_in_order()


if __name__ == '__main__':
    main()
