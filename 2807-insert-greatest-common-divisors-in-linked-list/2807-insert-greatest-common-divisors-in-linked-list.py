
import math

class Solution:
    def insertGreatestCommonDivisors(self, head):

        curr = head

        while curr and curr.next:

            # Calculate GCD of adjacent nodes
            gcd_value = math.gcd(curr.val, curr.next.val)

            # Create a new node
            new_node = ListNode(gcd_value)

            # Insert the new node
            new_node.next = curr.next
            curr.next = new_node

            # Move to the next original node
            curr = new_node.next

        return head
