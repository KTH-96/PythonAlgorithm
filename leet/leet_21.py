from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1

        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1
#         if not (list1 or list2):
#             return None
#         head1=list1
#         head2=list2
#         if not list1:
#             return head2
#         if not list2:
#             return head1
#         arr=[]
#         while head1:
#             arr.append(head1.val)
#             head1=head1.next
#         while head2:
#             arr.append(head2.val)
#             head2=head2.next
#         arr.sort()
#
#         newHead=ListNode(arr[0])
#         cur=newHead
#         for i in range(1,len(arr)):
#             cur.next=ListNode(arr[i])
#             cur=cur.next
#         return newHead
