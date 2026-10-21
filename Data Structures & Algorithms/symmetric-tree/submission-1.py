# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, root)]

        while(len(stack) > 0):
            toEvalR, toEvalL = stack.pop()
            if(toEvalR and not toEvalL):
                return False
            if(toEvalL and not toEvalR):
                return False
            if(not toEvalL and not toEvalR):
                continue
            if(toEvalL.val != toEvalR.val):
                return False
            stack.append((toEvalL.left, toEvalR.right))
            stack.append((toEvalL.right, toEvalR.left))
        
        return True


