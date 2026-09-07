"""LeetCode 104. 二叉树的最大深度 (Maximum Depth of Binary Tree) — Hot 100
难度：简单
递归终止条件对应空节点，左右子树结果取 max。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root: TreeNode) -> int:
    """递归计算左右子树最大深度。时间 O(n)，空间 O(h)。"""
    if not root:
        return 0
    return max(fun(root.left), fun(root.right)) + 1


if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert fun(root1) == 3, "示例1失败"
    assert fun(None) == 0, "空树测试失败"
    print("✅ E07 二叉树的最大深度 全部测试通过")
