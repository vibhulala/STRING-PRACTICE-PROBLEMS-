# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        '''
        brute force
        values=[]
        current=head
        #store all node values in described list 
        while current:
            values.append(current.val)
            current=current.next
        #put values back into linked list 
        values[left-1:right]=values[left-1:right][::-1]
        #put values back into linked list 
        current=head
        index=0
        while current:
            current.val=values[index]
            index+=1
            current=current.next
        return head
        time complexity-o(n)
        space complexity-o(n)
        '''
        if not head or left==right:
            return head
        #find the node just before the reversal section 
        dummy=ListNode(0)
        dummy.next=head
        before=dummy
        for _ in range (left-1):
            before=before.next
        #first node of the section that we will reverse
        first=before.next
        #reversig the required portion
        prev=None
        current=first
        for _ in range(right-left+1):
            #save
            next_node=current.next
            #change
            current.next=prev
            #move
            prev=current
            current=next_node
        #connecting the reversed section with remaining list
        before.next=prev
        first.next=current
        return dummy.next
        


