"""LeetCode 206. 反转链表 (Reverse Linked List) — Hot 100
难度：简单
元组解包可以在不引入临时变量的情况下反转指针。"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(head: ListNode) -> ListNode:
    """prev/cur 逐个反转。时间 O(n)，空间 O(1)。"""
    prev = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(3)))
    result1 = fun(head1)
    assert [result1.val, result1.next.val, result1.next.next.val] == [3, 2, 1], "示例1失败"
    assert fun(None) is None, "空链表测试失败"
    print("✅ E13 反转链表 全部测试通过")
