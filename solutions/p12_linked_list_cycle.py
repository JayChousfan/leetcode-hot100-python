"""
============================================================
LeetCode 141. 环形链表 (Linked List Cycle) — Hot 100
============================================================
难度：简单

题目：给你一个链表的头节点 head，判断链表中是否有环。
      如果某个节点可以通过连续跟踪 next 再次到达，则链表中存在环。

示例：
  输入: head = [3,2,0,-4], pos = 1
  输出: true
  解释: 链表尾部连接到下标为 1 的节点

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 同一对象的身份判断
   C++:  slow == fast
   Python: slow is fast
   → 两个引用指向同一节点时 is 为 True，不会调用对象的值比较逻辑

2. None 的短路判断
   C++:  while (fast != nullptr && fast->next != nullptr)
   Python: while fast is not None and fast.next is not None:
   → and 会短路；fast 为 None 时不会继续访问 fast.next

3. 布尔类型与字面量
   C++:  bool / true / false
   Python: bool / True / False
   → Python 的 True 和 False 首字母必须大写

4. 对象属性访问
   C++:  fast = fast->next->next;
   Python: fast = fast.next.next
   → Python 不区分对象和对象指针的成员访问，统一使用点号
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:
    """
    快慢指针同时出发；有环时快指针最终会追上慢指针。
    时间复杂度 O(n)，空间复杂度 O(1)
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        # slow 每次走一步，fast 每次走两步
        slow = slow.next
        fast = fast.next.next

        # is 判断两个引用是否指向同一个节点
        if slow is fast:
            return True

    return False


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert hasCycle(node1) is True, "示例1失败"
    assert hasCycle(ListNode(1)) is False, "单节点无环测试失败"
    assert hasCycle(None) is False, "空链表测试失败"
    print("✅ P12 环形链表 全部测试通过")
