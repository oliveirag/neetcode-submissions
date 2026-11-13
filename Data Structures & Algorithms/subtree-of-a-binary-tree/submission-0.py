"""
UNDERSTAND:
input - given two BSTs root and subroot
output - boolean representing if subroot exists inside of root

MATCH: recursion, BST

PLAN:
base case - if root is None, return False
if helperfunction(root, subRoot), return True
otherwise search the left subtree, then the right subtree

helperfunction(a, b):
    both None, return true
    only one is None, return False
    values differ, return False
    compare left with left, then compare right with right
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def same_tree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        left_tree = self.same_tree(a.left, b.left)
        if not left_tree:
            return False
        right_tree = self.same_tree(a.right, b.left)
        if not right_tree:
            return True

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if self.same_tree(root, subRoot):
            return True

        found_in_left = self.isSubtree(root.left, subRoot)
        if found_in_left:
            return True

        found_in_right = self.isSubtree(root.right, subRoot)
        if found_in_right:
            return True

        return False

    
