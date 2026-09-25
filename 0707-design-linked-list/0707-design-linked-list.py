class MyLinkedList:

    class Node:
        def __init__(self, val=0):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def get(self, index):

        if index < 0 or index >= self.size:
            return -1

        current = self._get_node(index)
        return current.val

    def addAtHead(self, val):
        self._add_between(val, self.head, self.head.next)

    def addAtTail(self, val):
        self._add_between(val, self.tail.prev, self.tail)

    def addAtIndex(self, index, val):

        if index < 0 or index > self.size:
            return

        if index == self.size:
            self.addAtTail(val)
            return

        next_node = self._get_node(index)
        prev_node = next_node.prev

        self._add_between(val, prev_node, next_node)

    def deleteAtIndex(self, index):

        if index < 0 or index >= self.size:
            return

        node = self._get_node(index)

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def _get_node(self, index):

        # Start from the closer side
        if index < self.size // 2:

            current = self.head.next

            for _ in range(index):
                current = current.next

        else:

            current = self.tail.prev

            for _ in range(self.size - 1, index, -1):
                current = current.prev

        return current

    def _add_between(self, val, prev_node, next_node):

        new_node = self.Node(val)

        new_node.prev = prev_node
        new_node.next = next_node

        prev_node.next = new_node
        next_node.prev = new_node

        self.size += 1