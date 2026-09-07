"""链表中倒数第 K 个节点 (Kth Node From End) — 字节真题
难度：简单
题目：返回链表中倒数第 k 个节点。
示例：[1,2,3,4,5], k=2 → 节点4
思路：fast 先走 k 步，再让 slow 和 fast 同时移动。"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(head, k):
    """快慢指针。时间 O(n)，空间 O(1)。"""
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert fun(head, 2).val == 4, "示例1失败"
    assert fun(head, 5).val == 1, "头节点测试失败"
    print("✅ P02 链表中倒数第 K 个节点 全部测试通过")
