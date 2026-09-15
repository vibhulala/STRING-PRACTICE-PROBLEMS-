# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        brute force approach:- isme hmne simply ek nayi linked list create ki jo ki empty thi now ab hmne cuurent=head assign karke diey gaye linked list pe while loop chalay aaur gar koi bhi element nahi hua equal diye gaye val ke barabar to use dummy mein connedct karnege after that jaise hi mila use nhai adda kreneg sir use hi add akrna hai jo equal na ho then we will retunr tha dummy.next part 
        dummy=ListNode(0)
        tail=dummy
        current=head
        while current:
            if current.val!=val:
                tail.next=ListNode(current.val)
                tail=tail.next
            current=current.next
        return dummy.next
        # but one thing is here that we are creating extra linked list for storing which is not fair for the probelm hence we will move to better 
        time compleity-o(n)
        space compexity -o(n)
        '''
         # Dummy node head deletion ko bhi normal case bana deta hai
        dummy = ListNode(0, head)

        previous = dummy

        while previous.next:

            # Agar next node ko remove karna hai
            if previous.next.val == val:
                previous.next = previous.next.next

            else:
                previous = previous.next

        return dummy.next