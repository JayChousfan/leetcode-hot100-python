"""LeetCode 101. 对称二叉树 (Symmetric Tree) — Hot 100
难度：简单
递归同时比较镜像位置的两个节点。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root: TreeNode) -> bool:
    """递归判断左右子树是否互为镜像。时间 O(n)，空间 O(h)。"""
    def check(left: TreeNode, right: TreeNode) -> bool:
        if not left or not right:
            return left is right
        return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)

    return check(root.left, root.right) if root else True


if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(2), TreeNode(2))
    assert fun(root1) is True, "示例1失败"
    print("✅ E06 对称二叉树 全部测试通过")
