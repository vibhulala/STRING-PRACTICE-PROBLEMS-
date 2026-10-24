
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        '''
        BRUTE FROCE APPRAOCH :- isme hmane length calculate ki hai pure linked list ki anda after that we had calculated length-n isse hamen trvaersl mein hlep hui and we traversed from length -n-1 jaise hi waha pahucha usko age ka ek node skip akrke connect kar diey jisse nth node delete ho gyie
        length = 0
        current = head

        # Step 1: Calculate the length
        while current:
            length += 1
            current = current.next

        # Step 2: Handle deletion of the head
        if length == n:
            return head.next

        # Step 3: Reach the node before the target
        current = head
        for _ in range(length - n - 1):
            current = current.next

        # Step 4: Skip the target node
        current.next = current.next.next

        return head
        '''
        dummy = ListNode(0,head)
        slow=fast=dummy
        #move fast n steps forward 
        for _ in range(n):
            fast=fast.next
        #moving both pointers until fast reaches to last node 
        while fast.next:
            slow=slow.next
            fast=fast.next
        #delete the target node 
        slow.next=slow.next.next
        return dummy.next

