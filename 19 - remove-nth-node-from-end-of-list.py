# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        j = head.next
        while j and n:
            j = j.next
            n -= 1
        if n:
            while head and n:
                head = head.next
                n -= 1
        else:
            while j:
                j = j.next
                i = i.next
            i.next = i.next.next
        return head
