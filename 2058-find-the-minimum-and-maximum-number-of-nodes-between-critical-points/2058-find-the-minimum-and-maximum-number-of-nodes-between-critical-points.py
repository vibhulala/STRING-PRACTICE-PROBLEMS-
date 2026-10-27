
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        positions = []
        current = head.next
        previous = head
        position = 2

        while current.next:
            if ((current.val > previous.val and current.val > current.next.val) or
                (current.val < previous.val and current.val < current.next.val)):
                positions.append(position)

            previous = current
            current = current.next
            position += 1

        if len(positions) < 2:
            return [-1, -1]

        min_distance = float('inf')

        for i in range(1, len(positions)):
            min_distance = min(
                min_distance,
                positions[i] - positions[i - 1]
            )

        max_distance = positions[-1] - positions[0]

        return [min_distance, max_distance]
