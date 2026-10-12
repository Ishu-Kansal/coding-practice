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
        if(head is None):
            return None
        oldToNew = {}
        newHead = Node(x=0, next=None, random=None)
        oldToNew[head] = newHead

        i = newHead
        orig = head
        while(orig is not None and i is not None):
            i.val = orig.val
            oldToNew[orig] = i
            if(orig.next):
                nextNode = Node(x=0, next=None, random=None)
                i.next = nextNode
                i = i.next
            orig = orig.next
        
        i = newHead
        orig = head

        while(orig is not None and i is not None):
            if(orig.random):
                i.random = oldToNew[orig.random]
            i = i.next
            orig = orig.next
        
        return newHead


