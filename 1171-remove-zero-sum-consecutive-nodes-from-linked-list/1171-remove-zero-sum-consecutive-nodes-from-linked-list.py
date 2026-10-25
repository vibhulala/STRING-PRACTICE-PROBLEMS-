class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prefix_map = {}

        curr = dummy
        prefix_sum = 0

        # Pass 1: Store the last node for each prefix sum
        while curr:
            prefix_sum += curr.val
            prefix_map[prefix_sum] = curr
            curr = curr.next

        # Pass 2: Skip zero-sum sublists
        curr = dummy
        prefix_sum = 0

        while curr:
            prefix_sum += curr.val
            curr.next = prefix_map[prefix_sum].next
            curr = curr.next

        return dummy.next