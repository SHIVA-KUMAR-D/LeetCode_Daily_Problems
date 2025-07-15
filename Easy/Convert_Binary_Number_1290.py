# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ls = []
        i=0
        res=0
        while head is not None:
            if head.val==1:
                ls.append(i+1)
            i+=1
            head=head.next
        for x in ls:
            res+= 2 ** (i-x)
        return res