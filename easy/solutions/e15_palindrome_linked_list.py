"""LeetCode 234. 回文链表 (Palindrome Linked List) — Hot 100
难度：简单
题目：判断链表从前往后和从后往前读取是否相同。
示例：[1,2,2,1] → True
思路：快慢指针找中点，再反转后半段比较。"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(head):
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
    assert fun(head1), "示例1失败"
    assert not fun(ListNode(1, ListNode(2))), "非回文测试失败"
    print("✅ E15 回文链表 全部测试通过")
