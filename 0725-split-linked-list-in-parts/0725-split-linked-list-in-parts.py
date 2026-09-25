class Solution:
    def splitListToParts(self, head, k):

        # Step 1: Find length
        n = 0
        current = head

        while current:
            n += 1
            current = current.next

        # Step 2: Find size of each part
        base = n // k
        extra = n % k

        result = []
        current = head

        # Step 3: Create each part
        for i in range(k):

            part_head = current

            # First 'extra' parts get one additional node
            size = base + (1 if i < extra else 0)

            # Move to the last node of this part
            for _ in range(size - 1):
                current = current.next

            # Disconnect this part from the remaining list
            if current:
                next_part = current.next
                current.next = None
                current = next_part

            result.append(part_head)

        return result