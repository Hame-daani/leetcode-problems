# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        O(N): time
        O(1): space
        """
        if not head:
            return head
        # counting length
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        # calculating number of rotation
        rotate_num = k % length
        if not rotate_num:
            return head
        # new_end will be at 't' index
        t = length - rotate_num - 1
        curr = head
        while t:
            curr = curr.next
            t -= 1
        new_end = curr
        new_head = curr.next
        # attaching old head to the last element
        while curr.next:
            curr = curr.next
        curr.next = head
        new_end.next = None
        return new_head
