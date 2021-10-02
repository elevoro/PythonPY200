from collections.abc import MutableSequence, Iterable
from node import Node
from typing import Optional, Any


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._head: Optional[Node] = None
        self._tail = self._head
        self._len = 0

        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        """Метод удаляет значение узла по указанному индексу"""
        if self._head is None:
            print("The list has no element to delete")
        elif index == 1:
            del_node = self._head
            self._head = self.step_by_step_on_nodes(index + 1)
            del del_node
        elif 0 < index > self._len:
            print("Index out of range")
        else:
            del_node = self.step_by_step_on_nodes(index)
            bef_node = self.step_by_step_on_nodes(index - 1)
            bef_node.next = del_node.next
            del del_node

            self._len -= 1

    def __len__(self) -> int:
        """ Возвращает длину связного списка """
        return self._len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def insert(self, index: int, value: Optional[Node]) -> None:
        """ Добавление элемента в связный список по указанному индексу """
        if not isinstance(value, (Node, type(None))):
            value = Node(value)
        insert_node = Node(value)

        if self._head is None:
            self._head = self._tail = insert_node
        else:
            if index == 1:
                self.linked_nodes(insert_node, self._head)
                #insert_node.next = self._head
                self._tail = self._head
                self._head = insert_node

        i = 1
        n = self._head
        while i < index - 1 and n is not None:
            n = n.next
            i = i + 1
        if n is None:
            print("Index out of range")
        else:
            self.linked_nodes(insert_node, n)
            n.next = value

        self._len += 1

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self.__setitem__(self._len, value)

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self.__setitem__(1, value)

class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ...
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.__len__())
print(ll)
#ll.__delitem__(1)
print(ll.__dict__)
ll.insert(3, 3)
print(ll)
print(ll.__dict__)
