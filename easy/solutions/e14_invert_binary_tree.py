"""LeetCode 226. 翻转二叉树 (Invert Binary Tree) — Hot 100
难度：简单
元组解包可直接交换左右子树。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root: TreeNode) -> TreeNode:
    """递归交换每个节点的左右孩子。时间 O(n)，空间 O(h)。"""
    if not root:
        return None
    root.left, root.right = fun(root.right), fun(root.left)
    return root


if __name__ == "__main__":
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    result1 = fun(root1)
    assert result1.left.val == 3 and result1.right.val == 1, "示例1失败"
    print("✅ E14 翻转二叉树 全部测试通过")
