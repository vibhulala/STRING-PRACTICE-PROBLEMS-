# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''
        better appraoch :- isme hmne pehle next node ki value ko copy karke current node mein dala fir skip kar diy anext node ko by removing it actual remove nahi ho rha bas pointer ak movement hai 
        node.val=node.next.val
        node.next=node.next.next
        '''
        node.val, node.next = node.next.val, node.next.next