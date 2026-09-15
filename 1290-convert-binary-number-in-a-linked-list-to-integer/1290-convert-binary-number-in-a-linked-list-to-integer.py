# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
      '''
      brute force appraoch :-isme hm values nam kk ek balnk list le rhe for storing the values of the linked list in  it linked list per traverse karnege ek ek karke and uski valeus ko values[] mein dalte  jayenge after that ham us list ko join kar deneg and we wil make a single list after that we will convert that list into bianry form by int('101',2) . this will give the first disadvantage as we are using the extra space in name of list and string hence we will imporeve this in our better approach 
      values=[]
      current=head
      while current:
        values.append(current.val)
        current=current.next
      binary="".join(map(str,values)) 
      ans=int(binary,2)
      return ans
      time complexity-o(n)
      space complexity-o(n)
      '''  
      ans=0
      current=head
      while current:
        ans=ans*2+current.val
        current=current.next
      return ans