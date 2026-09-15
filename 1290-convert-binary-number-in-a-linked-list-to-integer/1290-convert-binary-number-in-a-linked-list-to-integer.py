# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
      values=[]
      current=head
      while current:
        values.append(current.val)
        current=current.next
      binary="".join(map(str,values)) 
      ans=int(binary,2)
      return ans  