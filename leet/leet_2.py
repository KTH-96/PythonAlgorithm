from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2

        node1_list = []
        node2_list = []
        while node1:
            node1_list.append(node1.val)
            node1 = node1.next

        while node2:
            node2_list.append(node2.val)
            node2 = node2.next

        node1_list.reverse()
        node2_list.reverse()

        node1_str_list = list(map(str, node1_list))
        node2_str_list = list(map(str, node2_list))

        node1_str, node2_str = '', ''

        for i in range(0, len(node1_str_list)):
            node1_str += node1_str_list[i]

        for i in range(0, len(node2_str_list)):
            node2_str += node2_str_list[i]

        result_list = list(str(int(node1_str) + int(node2_str)))

        new_node = ListNode(result_list[len(result_list) - 1])
        cur_node = new_node

        for i in range(len(result_list) - 2, -1, -1):
            cur_node.next = ListNode(result_list[i])
            cur_node = cur_node.next

        return new_node
#     연결리스트 뒤집기
#     def reverseList(self, head: ListNode) -> ListNode:
#         node, prev = head, None
#         while node:
#             next, node.next = node.next, prev
#             prev, node = node, next
#
#         return prev
#
#     연결리스트를 리스트형태로 변환
#     def toList(self, node: ListNode) -> List:
#         list: List = []
#
#         while node:
#             list.append(node.val)
#             node = node.next
#
#         return list
#
#     리스트를 연결 리스트로형태로 변환
#     def toReversedLinkedList(self, result: str) -> ListNode:
#         prev: ListNode = None
#         for r in result:
#             node = ListNode(r)
#             node.next = prev
#             prev = node
#
#         return node
#
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         a = self.toList(self.reverseList(l1))
#         b = self.toList(self.reverseList(l2))
#
#         result_str = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
#
#         return self.toReversedLinkedList(str(result_str))
