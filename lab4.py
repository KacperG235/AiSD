from typing import Any, List, Callable, Union


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: any, children: List['TreeNode'] = None):
        if children is None:
            children = []
        self.value = value
        self.children = children

    def is_leaf(self) -> bool:
        if self.children == None:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        visit(self)
        for x in self.children:
            x.for_each_deep_first()


def visit(lista: TreeNode) -> None:
    for x in lista.children:
        print(x.value)


def main():
    node1 = TreeNode(13)
    node2 = TreeNode(2)
    node3 = TreeNode(55)
    drzewo = TreeNode(4)
    drzewo.add(node1)
    drzewo.add(node2)
    drzewo.add(node3)
    drzewo.for_each_deep_first(visit(drzewo))


if __name__ == '__main__':
    main()
