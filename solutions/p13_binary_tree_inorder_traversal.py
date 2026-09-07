"""
============================================================
LeetCode 94. 二叉树的中序遍历 (Binary Tree Inorder Traversal) — Hot 100
============================================================
难度：简单

题目：给定一个二叉树的根节点 root，返回它的中序遍历结果。
      中序遍历的访问顺序是：左子树、根节点、右子树。

示例：
  输入: root = [1,null,2,3]
  输出: [1,3,2]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. list 的 .pop() 用作栈
   C++:  stack<TreeNode*> nodes; nodes.push(node); nodes.pop();
   Python: nodes.append(node); node = nodes.pop()
   → append() 从末尾入栈，pop() 删除并返回末尾元素，二者都是 O(1)

2. 生成器与 yield
   C++:  通常把遍历结果逐个 push_back 到 vector
   Python: yield node.val
   → yield 每次产出一个值并暂停函数，可按需迭代而不必一次构造完整结果

3. yield from 委托迭代
   C++:  递归调用后手动合并结果
   Python: yield from inorderValues(root.left)
   → yield from 会逐个转发子生成器产生的值

4. Python 递归深度限制
   C++:  深递归主要受线程栈大小限制
   Python: sys.setrecursionlimit(limit)
   → Python 默认递归深度通常约为 1000；极深的树应优先使用迭代栈
"""

from typing import Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list[int]:
    """
    用显式栈模拟递归：一路压入左节点，弹出访问后转向右子树。
    时间复杂度 O(n)，空间复杂度 O(h)，h 为树高
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    curr = root

    while curr is not None or stack:
        # 一直向左走，并把沿途节点压栈
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        # 弹出并访问节点，然后转向右子树
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


def inorderValues(root: TreeNode) -> Iterator[int]:
    """
    使用递归生成器逐个产生中序遍历节点值，作为递归写法对照。
    时间复杂度 O(n)，空间复杂度 O(h)
    """
    if root is None:
        return

    yield from inorderValues(root.left)
    yield root.val
    yield from inorderValues(root.right)


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    root1 = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    result1 = inorderTraversal(root1)
    assert result1 == [1, 3, 2], f"示例1失败: {result1}"
    assert list(inorderValues(root1)) == [1, 3, 2], "递归生成器测试失败"
    assert inorderTraversal(None) == [], "空树测试失败"
    print("✅ P13 二叉树的中序遍历 全部测试通过")
