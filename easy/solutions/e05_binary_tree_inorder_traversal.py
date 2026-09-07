"""LeetCode 94. 二叉树的中序遍历 (Binary Tree Inorder Traversal) — Hot 100
难度：简单
题目：按“左子树、根节点、右子树”的顺序遍历二叉树。
示例：[1,null,2,3] → [1,3,2]
思路：用 list 模拟栈进行迭代遍历。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root):
    """显式栈模拟中序遍历。时间 O(n)，空间 O(h)。"""
    result = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    return result


if __name__ == "__main__":
    root1 = TreeNode(1, right=TreeNode(2, TreeNode(3)))
    assert fun(root1) == [1, 3, 2], "示例1失败"
    print("✅ E05 二叉树的中序遍历 全部测试通过")
