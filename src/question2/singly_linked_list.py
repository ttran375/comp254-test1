# -*- coding: utf-8 -*-


class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.head.element

    def last(self):
        if self.is_empty():
            return None
        return self.tail.element

    def add_first(self, e):
        newest = Node(e, next_node=self.head)
        self.head = newest
        if self.is_empty():
            self.tail = self.head
        self.size += 1

    def add_last(self, e):
        newest = Node(e)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next_node = newest
        self.tail = newest
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        answer = self.head.element
        self.head = self.head.next_node
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedList) or self.size != len(other):
            return False

        node1, node2 = self.head, other.head
        while node1 is not None:
            if node1.element != node2.element:
                return False
            node1, node2 = node1.next_node, node2.next_node

        return True

    def __str__(self):
        result = []
        node = self.head
        while node is not None:
            result.append(str(node.element))
            node = node.next_node
        return "(" + ", ".join(result) + ")"

    def split(self):
        if self.size == 0:
            return SinglyLinkedList(), SinglyLinkedList()

        mid = self.size // 2
        if self.size % 2 != 0:
            mid += 1

        first_half = SinglyLinkedList()
        second_half = SinglyLinkedList()

        current = self.head
        for _ in range(mid):
            first_half.add_last(current.element)
            current = current.next_node

        while current is not None:
            second_half.add_last(current.element)
            current = current.next_node

        return first_half, second_half


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.add_last(1)
    list1.add_last(2)
    list1.add_last(3)
    list1.add_last(4)
    list1.add_last(5)
    print("Original list 1:", list1)

    list2 = SinglyLinkedList()
    list2.add_last(1)
    list2.add_last(2)
    list2.add_last(3)
    list2.add_last(4)
    print("Original list 2:", list2)

    first_half1, second_half1 = list1.split()
    first_half2, second_half2 = list2.split()

    print("First half of list 1:", first_half1)
    print("Second half of list 1:", second_half1)

    print("First half of list 2:", first_half2)
    print("Second half of list 2:", second_half2)
