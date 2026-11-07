# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
UNDERSTAND:
input - root of a BST
output - root of same BST but with left and right child swapped

MATCH: recursion

PLAN:
base case: if root is None return None
we need a temp variable so that it doesn't assign the same value to different nodes
assign temp to root.left
root.left = recursive call of root.right
root.right = recursive call of temp
return root

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        temp = root.left

        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root
        