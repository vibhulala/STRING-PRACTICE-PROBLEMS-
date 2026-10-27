
class Solution:
    def mergeNodes(self, head):
        write = current = head.next

        while current:
            total = 0

            while current.val:
                total += current.val
                current = current.next

            write.val = total
            current = current.next
            write.next = current
            write = current

        return head.next
