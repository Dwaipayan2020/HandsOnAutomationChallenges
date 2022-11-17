"""Basic implementation of advanced data structure.
   The following stack implementation assumes that
   the beginning  of the list will hold the top element of the stack
"""


class StackTop0:
    """Basic implementation of advanced data structure
       stack --> using List where
       peek or top of the stack is oth element
       pops an element from the beginning of a stack
       pushes an element to the beginning of list items
       This implementation is very similar to
       pre-defined push-pop implementation in stack datastructure.
    """

    def __init__(self):
        self.items = []

    def __str__(self):
        """For printing the stack elements"""
        return ' '.join([str(i) for i in self.items])

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.items == []

    def push(self, item):
        """adds new item to first beginning of the list"""
        self.items.insert(0, item)

    def pop(self):
        """pops item from the first beginning of the list"""
        return self.items.pop(0)

    def peek(self):
        """Top element in the stack"""
        return self.items[0]

    def size(self):
        """Length of the stack or size of the list."""
        return len(self.items)

    def display_all_items(self):
        """Display all items in the list"""
        return self.items
