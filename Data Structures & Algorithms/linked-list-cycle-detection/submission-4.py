# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UNDERSTAND:
Input: linked list
Output: boolean
Edge cases: if linked list is empty

MATCH:
linked lists
two pointer

PLAN:
initialize slow and fast, while fast is not null and fast.next is not null,
move slow by one node, move fast by two nodes, if at any point slow is equal to fast,
there is a cycle, return true, otherwise return false
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
