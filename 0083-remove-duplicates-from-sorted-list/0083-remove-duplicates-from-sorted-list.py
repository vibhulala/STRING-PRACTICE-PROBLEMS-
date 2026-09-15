# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # Brute Force Approach:
# Traverse the linked list while storing every visited value in a set.
# If the current value is already present in the set, it is a duplicate,
# so remove the current node by changing the previous node's next pointer.
        if head is None:
            return head
        seen=set()
        current=head
        while current:
            if current.val in seen:
                previous.next=current.next
            else:
                seen.add(current.val)
                previous=current
            current=current.next
        return  head 
        time complexity=o(n)
        space complexity=o(n)
        '''
        '''
        BETTER APPRAOCH :-is approach mein hmne set ka integration completly hata idya hai simply while loop chalya aur dkete ja rhe ki ane wala element aur uske bad wala smae to nahi agr hua to uske age wale se current ko connect akr deneg and age badh jayenge agr same ya duplicate nahi rhe to simple next address se connect akr denge and return kar deneg head ko 
        if head is None or head.next is None :
            return head
        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head
        time complexity =o(n)
        space complexity=o(1)
        '''
        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head