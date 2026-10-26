
class Solution:
    def doubleIt(self, head):
        # Add a leading 1 if doubling may create an extra digit
        if head.val >= 5:
            head = ListNode(0, head)

        current = head

        while current:
            # Double the current digit
            current.val = current.val * 2

            # Carry comes from the next digit
            if current.next and current.next.val >= 5:
                current.val += 1

            # Keep only the last digit
            current.val %= 10
            current = current.next

        return head
