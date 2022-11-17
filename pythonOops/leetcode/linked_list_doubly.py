"""Doubly Linked List"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def getsize(self):
        temp = self.head
        while temp:
            temp = temp.next
            self.size += 1
        return self.size

    def getnode(self, index):
        index_counter = 0
        temp = self.head
        while temp:
            try:
                if index == index_counter:
                    return temp.data
                temp = temp.next
                index_counter += 1
            except ValueError as val_err:
                print(str(val_err))

    def update_node(self, index, ch_data):
        index_counter = 0
        temp = self.head
        while temp:
            try:
                if index == index_counter:
                    temp.data = ch_data
                temp = temp.next
                index_counter += 1
            except ValueError as val_err:
                print(str(val_err))

    def delete_node(self, n):
        fst = self.head
        for _ in range(n):
            fst = fst.next
        if fst.next is None:
            fst.prev.next = None
        else:
            fst.data = fst.next.data
            fst.next = fst.next.next
        # return self.head

    def to_tuple(self):
        lst = list()
        temp = self.head
        while temp:
            lst.append(temp.data)
            temp = temp.next
        return tuple(lst)

    def to_list(self):
        lst = list()
        temp = self.head
        while temp:
            lst.append(temp.data)
            temp = temp.next
        return lst


llist = LinkedList()

"""Creating the head node"""
llist.head = Node(1)
"""Creating a second node."""
second = Node(2)
"""Creating a third node."""
third = Node(3)
"""Creating a fourth node."""
fourth = Node(4)
"""Creating a fifth node."""
fifth = Node(5)

"""Linking the second node to head's next."""
llist.head.next = second
second.prev = llist.head

"""Linking the third node to second's next."""
second.next = third
third.prev = second

"""Linking the fourth node to third's next."""
third.next = fourth
fourth.prev = third

"""Linking the fifth node to fourth's next."""
fourth.next = fifth
fifth.prev = fourth

# llist.print_list()
# print('size: ', llist.getsize())
# print(llist.getnode(0))


# llist.update_node(1, 5)
print(llist.to_list())
print(llist.delete_node(0))
print(llist.to_list())
