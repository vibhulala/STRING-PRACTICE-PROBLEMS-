# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited =set()#creating an extra space for storing 
        current=head
        while current:
            if current in visited:
                return True
            visited.add(current)#mila to sidha visited set mein add karenege
            current=current.next#moving to next node 
            #reached null , so no cycle
        return False