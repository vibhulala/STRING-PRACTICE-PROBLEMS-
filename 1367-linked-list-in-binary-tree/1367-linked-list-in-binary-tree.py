class Solution:
    def isSubPath(self,head,root):
        #if linkedlist is fully matched
        if not head: 
            return head
        #if tree path ends before the list 
        if not root:
            return False
        # Try matching from the current tree node,
        # or search for another starting node.
        return (
            self.check(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )
    def check(self,head,root):
        #entire linked list is matched
        if not head:
            return True
        #tree path ended before the list 
        if not root:
            return False
        #current values do not matched
        if head.val!=root.val:
            return False
        #continue downward direction
        return (
            self.check(head.next,root.left) or
            self.check(head.next,root.right)
        )
