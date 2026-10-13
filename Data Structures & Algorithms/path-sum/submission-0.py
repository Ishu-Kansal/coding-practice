# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root is None):
            return False
        
        stack = [ [root, 0] ]

        while(len(stack) > 0):
            currNode, currSum = stack.pop()
            
            if(currNode and (currNode.left or currNode.right)):
                stack.append( [currNode.left, currSum + currNode.val] )
                stack.append( [currNode.right, currSum + currNode.val] )
            else:
                if(currNode and currNode.val + currSum == targetSum):
                    return True
                
        
        return False