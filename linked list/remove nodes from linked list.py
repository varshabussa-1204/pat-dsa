# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=write=ListNode(None,head)
        stack=[]
        curr=head
        while curr:
            while stack and stack[-1]<curr.val:
                stack.pop()
            stack.append(curr.val)
            curr=curr.next
        for node in stack:
            write.next=ListNode(node)
            write=write.next
        return dummy.next
