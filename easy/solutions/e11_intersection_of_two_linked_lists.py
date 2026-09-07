"""LeetCode 160. 相交链表 (Intersection of Two Linked Lists) — Hot 100
难度：简单
题目：找出两个单链表开始相交的节点。
示例：两个链表从节点8开始相交 → 返回节点8
思路：两个指针交换链表后会同时到达交点。"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(headA, headB):
    """双指针交换起点以消除长度差。时间 O(m+n)，空间 O(1)。"""
    cur_a, cur_b = headA, headB
    while cur_a is not cur_b:
        cur_a = cur_a.next if cur_a else headB
        cur_b = cur_b.next if cur_b else headA
    return cur_a


if __name__ == "__main__":
    common = ListNode(8, ListNode(4, ListNode(5)))
    head1 = ListNode(4, ListNode(1, common))
    head2 = ListNode(5, ListNode(6, ListNode(1, common)))
    assert fun(head1, head2) is common, "示例1失败"
    print("✅ E11 相交链表 全部测试通过")
