# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
UNDERSTAND:
input - root of BST
output - integer representing the maximum depth of the BST
edge cases: none

MATCH: BST, recursion

PLAN:
base case: if root is null, return 0
create variable for left and traverse left
create variable for right and traverse right
if left is greater than right
    return 1 + left
else:
    return 1 + right
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
            if root is None:
                return 0
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

            if left_depth > right_depth:
                return 1 + left_depth
            else:
                return 1 + right_depth
        
