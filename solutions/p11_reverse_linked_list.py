"""
============================================================
LeetCode 206. 反转链表 (Reverse Linked List) — Hot 100
============================================================
难度：简单

题目：给你单链表的头节点 head，请你反转链表，并返回反转后的链表。

示例：
  输入: head = [1,2,3,4,5]
  输出: [5,4,3,2,1]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 类与 __init__ 构造函数
   C++:  struct ListNode { int val; ListNode* next; };
   Python: class ListNode: def __init__(self, val=0, next=None): ...
   → 构造函数名固定为 __init__，self 相当于 C++ 的 this

2. 对象属性访问
   C++:  head->val, head->next
   Python: head.val, head.next
   → Python 用点号访问属性，对象变量本身就是引用

3. None 对应 nullptr
   C++:  ListNode* prev = nullptr;
   Python: prev = None
   → None 是 Python 的空值，首字母必须大写

4. 多变量同时赋值
   C++:  需要临时变量保存 cur->next
   Python: cur.next, prev, cur = prev, cur, cur.next
   → 右侧先按旧值计算，再依次赋给左侧，不需要临时变量

5. 链表节点创建
   C++:  new ListNode(1)
   Python: ListNode(1)
   → Python 没有 new 关键字，直接调用类名即可
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    """
    迭代法：用 prev/cur 双指针逐个反转节点。
    时间复杂度 O(n)，空间复杂度 O(1)
    """
    prev = None
    cur = head

    while cur:
        cur.next, prev, cur = prev, cur, cur.next

    return prev


def build_list(nums: list[int]) -> ListNode:
    """将列表转换为链表，方便测试。"""
    dummy = ListNode(0)
    cur = dummy

    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next


def to_list(head: ListNode) -> list[int]:
    """将链表转换为列表，方便断言。"""
    result: list[int] = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    head1 = build_list([1, 2, 3, 4, 5])
    assert to_list(reverseList(head1)) == [5, 4, 3, 2, 1], "示例1失败"
    head2 = build_list([1, 2])
    assert to_list(reverseList(head2)) == [2, 1], "两节点测试失败"
    assert reverseList(None) is None, "空链表测试失败"
    head4 = build_list([1])
    assert to_list(reverseList(head4)) == [1], "单节点测试失败"
    print("✅ P11 反转链表 全部测试通过")
