# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UNDERSTAND:
input - linked list
output - linked list without duplicates
edge cases - empty list, return empty list

MATCH: linked list, two pointer

PLAN:
if empty list, return empty
initialize current
while current is not null:
    if current.val == current.next.val:
        current.next == current.next.next
    current = current.next
return head

"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
