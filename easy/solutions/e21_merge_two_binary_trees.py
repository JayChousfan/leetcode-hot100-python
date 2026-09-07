"""LeetCode 617. 合并二叉树 (Merge Two Binary Trees) — Hot 100
难度：简单
递归同时处理两棵树的对应节点。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root1, root2):
    """将对应节点值相加并递归合并左右子树。时间 O(m+n)，空间 O(h)。"""
    if not root1:
        return root2
    if not root2:
        return root1

    root1.val += root2.val
    root1.left = fun(root1.left, root2.left)
    root1.right = fun(root1.right, root2.right)
    return root1


if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(3), TreeNode(2))
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    result1 = fun(root1, root2)
    assert result1.val == 3 and result1.left.val == 4 and result1.right.val == 5, "示例1失败"
    print("✅ E21 合并二叉树 全部测试通过")
