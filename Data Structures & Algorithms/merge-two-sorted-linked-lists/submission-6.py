# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UNDERSTAND:
input - two lists
output - merged list
edge cases - if both lists are empty

MATCH: linked lists, two pointer

PLAN:
(BOTH LISTS ARE ALREADY SORTED)
handle edge cases for empty linked lists
create two pointers, one for l1 the other for l2
walk thru both lists at the same times comparing values
if val at list 2 is less than val at list 1, add that to list 1 and adjust pointers
go thru entire list and return list 1

"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if list1 and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
    
        dummy = ListNode() # create a new node
        current = dummy # create pointer

        # walk thru both lists attaching correct values
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

        # attach any remaining nodes
        current.next = list1 or list2

        return dummy
      
    

        