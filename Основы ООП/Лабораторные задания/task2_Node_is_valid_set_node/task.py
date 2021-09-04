from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (Node, type(None))):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next = next_


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.set_next(node_2)
    node_2.set_next(node_3)
    print(node_1, node_2)
