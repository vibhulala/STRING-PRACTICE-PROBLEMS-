# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        current = head

        while current:

            # Next node ko save karo
            next_node = current.next

            # Current node ka link reverse karo
            current.next = previous

            # Pointers ko aage move karo
            previous = current
            current = next_node

        return previous