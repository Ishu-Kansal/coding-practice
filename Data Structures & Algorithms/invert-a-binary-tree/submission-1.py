# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(currNode):
            if(not currNode):
                return None
            temp = currNode.left
            currNode.left = invert(currNode.right)
            currNode.right = invert(temp)
            return currNode
        
        return (invert(root))
