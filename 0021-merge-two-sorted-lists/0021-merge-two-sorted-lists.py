# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        values=[]
        current=list1
        while current:
            values.append(current.val)
            current=current.next
        current=list2
        while current:
            values.append(current.val)
            current=current.next
        values.sort()
        #creating a new linked list 
        dummy=ListNode(0)
        tail=dummy
        for value in values:
            tail.next=ListNode(value)
            tail=tail.next
        return dummy.next
        