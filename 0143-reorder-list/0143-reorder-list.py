
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # 3. Merge both halves
        first, second = head, prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second
