# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UNDERSTAND:
input - linked list
output - same linked list but in a specific order
edge cases - if linked list has one node

MATCH: linked list, two pointer

[1, 2, 3, 4, 5]
middle = 3
first half -> 1, 2, 3
second half -> 4, 5
reverse second half -> 5, 4
weave: [1, 5, 2, 4, 3]


PLAN: 
find the middle, first half gets the extra node where n is odd
split the list
reverse second half, so its first node is the original last node
first half node, second half node, first half node, second half node

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        middle = self.find_middle(head)

        second_half = middle.next
        middle.next = None # cut the list

        second_half = self.reverse(second_half)
        self.merge(head, second_half)

    def find_middle(self, head):
        # when fast hits the end slow is in the middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        # reverses the second half
        previous = None
        current = head
        while current:
            walker = current.next
            current.next = previous
            previous = current
            current = walker
        return previous

    def merge(self, first, second):
        # first half is the same length as second, or one node longer
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next





        