
class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prefix_sum = 0
        last_seen = {}
        current = dummy

        # Pass 1: Store the last node for each prefix sum
        while current:
            prefix_sum += current.val
            last_seen[prefix_sum] = current
            current = current.next

        # Pass 2: Skip zero-sum ranges
        prefix_sum = 0
        current = dummy

        while current:
            prefix_sum += current.val
            current.next = last_seen[prefix_sum].next
            current = current.next

        return dummy.next
