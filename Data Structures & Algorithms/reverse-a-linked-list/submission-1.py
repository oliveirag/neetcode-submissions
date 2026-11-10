# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UNDERSTAND:
input - linked list
output - new linked list but reversed
edge cases - if list is empty

MATCH: linked lists and two pointers

PLAN:
handle edge case if list is empty
intialize prev, curr
while current != None:
    move each pointer
    

"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev





        