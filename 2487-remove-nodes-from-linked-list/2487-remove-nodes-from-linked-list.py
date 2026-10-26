
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        '''
        BRUTE FORCE APPROACH 
        dummy = ListNode(0, head)
        current = dummy

        while current.next:
            target = current.next
            runner = target.next
            found_greater = False

            while runner:
                if runner.val > target.val:
                    found_greater = True
                    break
                runner = runner.next

            if found_greater:
                current.next = target.next
            else:
                current = current.next

        return dummy.next
        TIME COMPLEXITY-O(N^2)
        SPACE COMPLEXITY-0(N)
        '''
        #revrsing the linked list first 
        prev=None 
        current=head 
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        head =prev
        #now we will find the greater value
        maximum=head.val
        current=head
        while current.next :
            if current.next.val<maximum:
                current.next=current.next.next
            else:
                current=current.next
                maximum=current.val
        #reverse the linked list back after deleteing the lesser elements 
        prev=None 
        current =head 
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        return prev 

