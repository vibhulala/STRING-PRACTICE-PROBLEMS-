class Solution:
    def flatten(self, head):

        if not head:
            return head

        current = head

        while current:

            if current.child:

                child = current.child
                next_node = current.next

                # Connect current with child
                current.next = child
                child.prev = current

                # Find the end of child list
                last = child

                while last.next:
                    last = last.next

                # Connect child list with original next
                if next_node:
                    last.next = next_node
                    next_node.prev = last

                # Remove child pointer
                current.child = None

            current = current.next

        return head