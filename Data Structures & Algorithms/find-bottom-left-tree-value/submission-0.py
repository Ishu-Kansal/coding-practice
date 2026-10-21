# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        deepest = 0
        deepestVal = 0

        stack = [(root, 1)]
        
        while(len(stack) > 0):
            currNode, currDepth = stack.pop()
            if(not currNode):
                continue
            if(currDepth > deepest):
                deepest = currDepth
                deepestVal = currNode.val
            stack.append((currNode.right, currDepth + 1))
            stack.append((currNode.left, currDepth + 1))
            
        
        return deepestVal
            
