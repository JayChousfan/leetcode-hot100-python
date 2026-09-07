"""LeetCode 141. 环形链表 (Linked List Cycle) — Hot 100
难度：简单
题目：判断链表中是否存在环。
示例：[3,2,0,-4], 尾节点连接下标1 → True
思路：快慢指针相遇说明存在环。"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(head):
    """Floyd 快慢指针判环。时间 O(n)，空间 O(1)。"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2))
    head1.next.next = head1
    assert fun(head1), "有环测试失败"
    assert not fun(ListNode(1)), "无环测试失败"
    print("✅ E10 环形链表 全部测试通过")
