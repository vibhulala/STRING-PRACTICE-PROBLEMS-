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
      '''
      better approch:- ko hmne better aise bana by making the calculations during the time of traverssal of linekd list we will simply make a binary to deciamal calcualtion liek 101 if we pikk 1 we will do this 0*2+1=1 and so on ... 
      ans=0
      current=head
      while current:
        ans=ans*2+current.val
        current=current.next
      return ans
      time complexity -o(n)
      space complexity -O(1)
      '''
      # WAISE TO BETTER HI OPTIMIZED THA BUT FIR BHI ISE AUR PYTHONIC BAN SKTE HAIN 
      ans = 0
      while head:
        ans = ans * 2 + head.val
        head = head.next
      return ans
