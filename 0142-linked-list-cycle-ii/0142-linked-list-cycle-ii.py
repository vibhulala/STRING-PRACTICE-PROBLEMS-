
class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head

        # Phase 1: Detect whether a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            return None

        # Phase 2: Find the cycle's starting node
        slow = head

        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow
