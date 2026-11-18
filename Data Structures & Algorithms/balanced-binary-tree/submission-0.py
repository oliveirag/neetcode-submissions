# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
UNDERSTAND:
input - root of BST
output - boolean representing whether tree is height-balanced
edge cases - empty BST

MATCH: BST and recursion

PLAN:
create helper function
if node is None, return 0

calculate the height of left and right:

left = recursive call of node.left
if subtree is unbalanced, return -1

right = recursive call of node.right
if subtree is unbalanced, return -1

if the height difference is greater than 1, return -1
otherwise, return the current node's height

only return false if the helper function returns -1
if the helper function returns any other number, return true

"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1
            
            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
        
        return dfs(root) != -1
