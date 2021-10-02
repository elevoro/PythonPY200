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
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    # def __str__(self) -> str:
    #     return str(self.value)

    def __is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.__is_valid(next_)
        self._next = next_

class DoubleLinkedNode(Node):
    """ Класс, который описывает узел двусвязного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev_: Optional["Node"] = None):
        """
        Создаем новый узел для двусвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        :param prev_: предыдущий узел, если он есть
        """
        super().__init__(value, next_)
        self._prev = prev_

    def __repr__(self) -> str:
        return f"Node({None}, {self.value}, {None})" \
            if self._next and self._prev is None else f"Node({None}, {self.value}, {self.next})" \
            if self._next is not None and self._prev is None else f"({self._prev}, {self.value}, {None})" \
            if self._next is None and self._prev is not None else f"({self._prev}, {self.value}, {self.next})"

    @property
    def prev(self):
        return self.prev

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        self.__is_valid(prev_)
        self.prev = prev_


node_1 = Node('ffhfh')
node_2 = Node(2)
print(node_2)
node_4 = Node(4)
first_node = DoubleLinkedNode(2)
second_node = DoubleLinkedNode(3, node_4, node_2)
next_node = DoubleLinkedNode(1, node_2)
print(next_node)
