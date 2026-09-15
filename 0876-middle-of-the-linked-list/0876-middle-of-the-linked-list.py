# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        bruute force :- isme hmne pehle length nikali diye hue poore linked list ki fir length calculate karne ke badd middle part chiaye to //2 kar diye length ko after that hmne jo length ayi wahase end tk traverse karek wahi part return kar diye 
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        middle=length//2
        current=head
        for _ in range(middle):
            current=current.next
        return current
        time complexity-o(n)
        space complexity-o(1)

        '''
        slow = head
        fast = head

        while fast and fast.next:

            # Slow moves one step
            slow = slow.next

            # Fast moves two steps
            fast = fast.next.next

        return slow