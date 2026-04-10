# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # for 0 - 9, create a node for each number

        
        head_copy = ListNode()
        curr = head_copy
        head_copy.next = curr
        carry_on = 0

        while l1 or l2 or carry_on:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            sum = v1 + v2 + carry_on
            carry_on = int(sum / 10)
            print(carry_on)
            remainder = sum % 10


            tmp_node = ListNode(remainder)
            curr.next = tmp_node

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head_copy.next
            


            
