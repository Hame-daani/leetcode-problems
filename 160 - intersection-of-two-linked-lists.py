# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # return self.first(headA, headB)
        return self.second(headA, headB)

    def first(self, headA, headB):
        """
        O(M+N): slower
        O(1)
        """
        m = 0
        curr = headA
        while curr:
            curr = curr.next
            m += 1
        n = 0
        curr = headB
        while curr:
            curr = curr.next
            n += 1
        if m > n:
            for _ in range(m - n):
                headA = headA.next
        elif n > m:
            for _ in range(n - m):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

    def second(self, headA, headB):
        """
        O(M+N): faster
        O(1)
        """
        a = headA
        b = headB
        while a != b:
            # exit case if no intersection, a == b == None
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
