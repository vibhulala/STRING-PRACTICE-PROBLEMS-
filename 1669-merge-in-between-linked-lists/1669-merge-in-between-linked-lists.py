class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next

        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next

        tail_b = list2
        while tail_b.next:
            tail_b = tail_b.next

        prev_a.next = list2
        tail_b.next = after_b

        return list1