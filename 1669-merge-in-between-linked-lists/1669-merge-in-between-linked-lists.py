# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #sabse pehle prev_a identify hoga 
        prev_a=list1
        for _ in range(a-1):
            prev_a=prev_a.next
        # ab hm after_b find karenge 
        after_b=list1
        for _ in range(b+1):
            after_b=after_b.next
        #ab tail find karnege list2 ki 
        tail_b=list2
        while tail_b.next:
            tail_b=tail_b.next
        #now we will join the both the lists 
        prev_a.next=list2
        tail_b.next=after_b
        return list1