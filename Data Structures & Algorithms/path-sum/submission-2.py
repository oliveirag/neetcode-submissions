"""
UNDERSTAND:
input - BST root
output - boolean representing if the root to leaf path equals targetSum

MATCH: recursion, BST

PLAN:
if root is null, return false
remaining = targetSum - root.val
if root.left is None and root.right is None:
    if remaining == 0:
        return True
    return False
found_left = recursive call
    if found_left is true, return true
found_right = recursive call
    if found_right is true, return true
return false


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        remaining = targetSum - root.val

        if root.left is None and root.right is None:
            if remaining == 0:
                return True
            return False

        found_left = self.hasPathSum(root.left, remaining)
        if found_left:
            return True

        found_right = self.hasPathSum(root.right, remaining)
        if found_right:
            return True

        return False
        

