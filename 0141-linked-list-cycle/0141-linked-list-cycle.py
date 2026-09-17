# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        brute froce :- isme hmne ek extra memory set ke nam pe li hai karn ayeh hai ki list ko traverse akrneeg aur dekhenge ki set me wo element hai ya anhi agr nahi hua to hme usme append kar denge aur last mein agr null mill gya tp return False
        visited =set()#creating an extra space for storing 
        current=head
        while current:
            if current in visited:
                return True
            visited.add(current)#mila to sidha visited set mein add karenege
            current=current.next#moving to next node 
            #reached null , so no cycle
        return False
        time complexity -o(n)
        space complexity-o(n)
        '''
        slow=fast=head
        while fast and fast.next:
            slow=slow.next#slow moves one step
            fast=fast.next.next#fast moves two steps
            if slow is fast:#agar dono pointers mill gaye to cycle exists hogi
                return True
        #fast reached NULL , to koi cycle nahi banegi
        return False
