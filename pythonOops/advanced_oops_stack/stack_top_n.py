"""Basic implementation of advanced data structure.
   The following stack implementation assumes that
   the end of the list will hold the top element of the stack
"""


class StackTopn:
    """Basic implementation of advanced data structure
       stack --> using List where
       peek of the stack is nth element.
       pops an element from top
       pushes an element to the top.
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
        """adds new item to top end of the list"""
        self.items.append(item)

    def pop(self):
        """pops item from the top end of the list"""
        return self.items.pop()

    def peek(self):
        """Top element in the stack"""
        return self.items[len(self.items) - 1]

    def size(self):
        """Length of the stack or size of the list."""
        return len(self.items)

    def display_all_items(self):
        """Display all items in the list"""
        return self.items
