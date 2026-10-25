
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head:
            return

        nodes = []
        current = head

        # Store all nodes in an array
        while current:
            nodes.append(current)
            current = current.next

        left, right = 0, len(nodes) - 1

        # Reorder nodes from both ends
        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left >= right:
                break

            nodes[right].next = nodes[left]
            right -= 1

        # Terminate the list
        nodes[left].next = None
