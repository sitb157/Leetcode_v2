# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_list_1 = [l1.val]
        while l1.next != None:
            l1 = l1.next
            node_list_1.append(l1.val)

        node_list_2 = [l2.val]
        while l2.next != None:
            l2 = l2.next
            node_list_2.append(l2.val)
        l1_num = 0
        l2_num = 0
        for idx, l in enumerate(node_list_1):
            l1_num += l*10**idx
        for idx, l in enumerate(node_list_2):
            l2_num += l*10**idx
        total_num = l1_num + l2_num
        total_str = f"{total_num}"
        total_head = ListNode()
        total_l = total_head
        total_l.val = int(total_str[-1])
        for idx in range(len(total_str)-2, -1, -1):
            total_l.next = ListNode()
            total_l = total_l.next
            total_l.val = int(total_str[idx])
        return total_head