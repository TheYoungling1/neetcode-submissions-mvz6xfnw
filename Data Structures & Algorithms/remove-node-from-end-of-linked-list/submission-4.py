# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Reverse the linked list, 
        # delete the first n nodes
        # reverse again 
        # return head

        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 1. Move right pointer forward by n steps
        for _ in range(n):
            right = right.next
            
        # 2. Move both pointers until right falls off the end of the list
        while right is not None:
            right = right.next
            left = left.next
        print(left.val)
            
        # 3. left is now sitting EXACTLY before the node we want to delete
        left.next = left.next.next
        
        # Return dummy.next, which is the true head of our list
        return dummy.next

            



