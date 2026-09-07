"""LeetCode 234. 回文链表 (Palindrome Linked List) — Hot 100
难度：简单
快慢指针找中点，再原地反转后半段。"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(head: ListNode) -> bool:
    """比较前半段与反转后的后半段。时间 O(n)，空间 O(1)。"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert fun(head1) is True, "示例1失败"
    assert fun(ListNode(1, ListNode(2))) is False, "非回文测试失败"
    print("✅ E15 回文链表 全部测试通过")
