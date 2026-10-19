# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        '''
        if not head or not head.next:
            return None
        #calculating the length 
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        #finding the middle of the linked list 
        middle=length//2
        #traversing till one node before of the middle
        prev=head
        for _ in range(middle-1):
            prev=prev.next
        #delete the middle or skipp the middle node 
        prev.next=prev.next.next
        return head  
        '''
        '''
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        prev.next = slow.next

        return head
        '''
        if not head or not head.next:
            return None

        prev = None
        slow = fast = head

        while fast and fast.next:
            prev, slow = slow, slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head



