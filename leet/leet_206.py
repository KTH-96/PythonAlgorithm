from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        node = head

        if not head:
            return node

        node_list = []

        while node:
            node_list.append(node.val)
            node = node.next

        new_head = ListNode(node_list[len(node_list) - 1])
        cur_node = new_head

        for i in range(len(node_list) - 2, 0, -1):
            cur_node.next = ListNode(node_list[i])
            cur_node = cur_node.next

        return new_head
    # node, prev = head, None
    #
    #         if not head:
    #             return node
    #
    #         while node:
    #             next, node.next = node.next, prev
    #             prev, node = node, next
    #
    #         return prev
