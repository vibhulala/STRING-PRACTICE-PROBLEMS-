# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        '''
        brute force:-isme hmne ek empty list le li hai ab jo hai current linked list se ek ek values nikal ke values mein append karnege aur ek list ban jaeygi fir usko reverse karke compare karenge original wale se 
        values=[]
        current=head
        while current:
            values.append(current.val)
            current=current.next
        return values==values[::-1]
        time complexity-o(n)
        space complexity-o(n)
        '''
        slow = fast = head

        # Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
        