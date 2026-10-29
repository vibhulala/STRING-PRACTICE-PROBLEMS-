class Solution:
    def modifiedList(self, nums, head):
        values = set(nums)

        dummy = ListNode(0, head)
        current = dummy

        while current.next:
            if current.next.val in values:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next