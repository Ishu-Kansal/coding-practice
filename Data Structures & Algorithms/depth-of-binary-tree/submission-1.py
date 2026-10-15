# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def getDepth(currNode):
            if(currNode is None):
                return 0
            if(currNode.left is None and currNode.right is None):
                return 1
            
            return max(getDepth(currNode.left), getDepth(currNode.right)) + 1
        
        return getDepth(root)