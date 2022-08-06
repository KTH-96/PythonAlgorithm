# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = []

        if not head:
            return False

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        left, right = 0, len(q) - 1

        while left < right:
            if q[left] != q[right]:
                return False
            left += 1
            right -= 1

        return True
