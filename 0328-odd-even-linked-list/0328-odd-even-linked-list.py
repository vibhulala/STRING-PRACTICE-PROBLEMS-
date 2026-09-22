# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        '''
        brute force appraoch:= so in brute force emin hmne pointers ka koi concept nahi lya we just start with simple seggregation ki linked list node mein jo bhi odd indices pe hain unhe odd list mein append kiya and even indices walon ko even list mein append kiya so isse yeh clear hua ki hmne unhe apend karke add kiya after that hmne us list ke elemnst ko finally ek linked list mein convert kiya 
        if not head:
            return head
        odd=[]
        even=[]
        current=head
        position=1
        while current:
            if position%2==1:
                odd.append(current.val)
            else:
                even.append(current.val)
            current=current.next
            position+=1
        values=odd+even
        #creating the rearranged linked list
        current=head
        index=0
        while current:
            current.val=values[index]
            index+=1
            current=current.next
        return head
        time complexity -o(n)
        space complexity-o(n) space due to use of list/array in this 
        '''
        if not head or not head.next: 
            return head
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head

