"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Fist initialise the array as Null

        # Stores the curr index and random index 
        if not head:
            return None

        # Map: Old Node -> New Node
        # We handle None here so pt_dict.get(None) returns None automatically
        pt_dict = {None: None}

        # First Pass: Create all nodes and store them in the map
        curr = head
        while curr:
            pt_dict[curr] = Node(curr.val)
            curr = curr.next

        # Second Pass: Connect next and random pointers
        curr = head
        while curr:
            copy = pt_dict[curr]
            copy.next = pt_dict[curr.next]
            copy.random = pt_dict[curr.random]
            curr = curr.next

        return pt_dict[head]


