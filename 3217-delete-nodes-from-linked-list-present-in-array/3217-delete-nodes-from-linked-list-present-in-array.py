# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values=set(nums)
        while head and head.val in values:
            head=head.next
        previous=head
        current=head.next if head else None
        while current:
            if current.val in values:
                previous.next=current.next
            else:
                previous=current
            current=current.next
        return head