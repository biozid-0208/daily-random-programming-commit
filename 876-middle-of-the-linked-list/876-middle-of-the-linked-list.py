# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fPtr = head
        sPtr = head
        counter = 0
        result = []
        while(fPtr):
            fPtr = fPtr.next
            counter += 1
        for i in range(0, counter//2 ):
            sPtr = sPtr.next
        return sPtr
            
            
            
        