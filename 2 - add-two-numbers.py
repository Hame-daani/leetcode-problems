# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode((l1.val + l2.val) % 10)
        node1 = l1.next
        node2 = l2.next
        carry = (l1.val + l2.val) // 10
        node = res
        while node1 and node2:
            node.next = ListNode((carry + node1.val + node2.val) % 10)
            carry = (carry + node1.val + node2.val) // 10
            node = node.next
            node1 = node1.next
            node2 = node2.next
        if not node1:
            while node2:
                node.next = ListNode((carry + node2.val) % 10)
                carry = (carry + +node2.val) // 10
                node = node.next
                node2 = node2.next
        if not node2:
            while node1:
                node.next = ListNode((carry + node1.val) % 10)
                carry = (carry + +node1.val) // 10
                node = node.next
                node1 = node1.next
        if carry:
            node.next = ListNode(carry)
        return res
