"""LeetCode 101. 对称二叉树 (Symmetric Tree) — Hot 100
难度：简单
题目：判断一棵二叉树是否左右镜像对称。
示例：[1,2,2,3,4,4,3] → True
思路：递归比较两个镜像位置的节点。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root):
    """递归判断左右子树是否互为镜像。时间 O(n)，空间 O(h)。"""
    def check(left, right):
        if not left or not right:
            return left is right
        return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)

    return check(root.left, root.right) if root else True


if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(2), TreeNode(2))
    assert fun(root1), "示例1失败"
    print("✅ E06 对称二叉树 全部测试通过")
