# # Merge two sorted linkedlist list
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         prehead = ListNode(-1)
#
#         prev = prehead
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 prev.next = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 l2 = l2.next
#             prev = prev.next
#
#         # At least one of l1 and l2 can still have nodes at this point, so connect
#         # the non-null list to the end of the merged list.
#         prev.next = l1 if l1 is not None else l2
#
#         return prehead.next.val + prev.next.val
#
# list1 = ListNode([1,2])
# list2 = ListNode([2,3])
#
# sol = Solution()
# sol.mergeTwoLists(list1,list2)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        seen = set()
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        current_node = head

        while current_node:
            if current_node.val in seen:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                seen.add(current_node.val)
                prev_node = current_node
                current_node = current_node.next

        return dummy.next
list = ListNode([1,2,1,2])

sol = Solution()
sol.deleteDuplicates(list)
