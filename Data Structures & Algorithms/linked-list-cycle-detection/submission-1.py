# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointer, eventually the fast pointer will
        # Lap the slow

        # We start the fast pointer to be ahead of the slow pointer, 
        # if the index of the fast pointer is lower than the slow pointer
        # then there is a cycle.

        # As we dont have index in linked list, we can also check this condition
        # by if the fast pointer and slow pointer points to the same
        # none null node (as they have a common factor...)
        
        # 1. The Gap Closes by 2If the slow pointer moves 1 step and the fast pointer moves 3 steps,
        #  the relative speed is 2. This means the gap between them closes by 2 nodes every iteration.
        #  Because it closes by 2, the outcome depends on the distance between them:If the distance is an
        # EVEN number (e.g., 4): The distance goes $4 \rightarrow 2 \rightarrow 0$. They land on the exact 
        # same node.If the distance is an ODD number (e.g., 3): The distance goes $3 \rightarrow 1 \rightarrow -1$.
        #  The fast pointer just jumped right over the slow pointer!


        slow = head
        fast = head

        # As long as fast exists AND the node after fast exists...
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            # Compare the nodes themselves, not their values
            if slow == fast:
                return True
                
        # If the loop breaks, fast reached the end of the list. No cycle!
        return False
            


