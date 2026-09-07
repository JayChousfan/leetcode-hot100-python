"""LeetCode 21. 合并两个有序链表 (Merge Two Sorted Lists) — Hot 100
难度：简单
Python 对象引用对应 C++ 指针，dummy 简化头节点处理。"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fun(list1, list2):
    """依次连接较小节点。时间 O(m+n)，空间 O(1)。"""
    dummy = ListNode()
    cur = dummy
    while list1 and list2:
        if list1.val < list2.val:
            cur.next, list1 = list1, list1.next
        else:
            cur.next, list2 = list2, list2.next
        cur = cur.next
    cur.next = list1 or list2
    return dummy.next


def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    assert to_list(fun(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4], "示例1失败"
    print("✅ E03 合并两个有序链表 全部测试通过")
