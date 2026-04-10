# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # --- PHASE 1: Find the middle ---
        slow = head
        fast = head
        
        # Checking fast and fast.next is the safest way to avoid None errors
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # --- PHASE 2: Reverse the second half ---
        curr = slow.next
        slow.next = None  # Sever the first half from the second half!
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node  # Move forward using the saved node

        # --- PHASE 3: Merge the two halves in-place ---
        list1 = head
        list2 = prev  # prev is the new head of the reversed second half
        
        # Since we split it evenly, list2 will always hit None first or at the same time
        while list2:
            # 1. Save the next pointers so we don't lose the rest of the lists
            next1 = list1.next
            next2 = list2.next
            
            # 2. Make the alternating connections
            list1.next = list2
            list2.next = next1
            
            # 3. Advance both pointers forward for the next iteration
            list1 = next1
            list2 = next2
            
        # No return statement needed, we modified the list in-place!
        

            

        
        

        