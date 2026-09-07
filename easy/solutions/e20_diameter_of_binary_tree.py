"""LeetCode 543. 二叉树的直径 (Diameter of Binary Tree) — Hot 100
难度：简单
题目：求二叉树中任意两个节点之间最长路径的边数。
示例：[1,2,3,4,5] → 3
思路：递归求深度，同时更新左右深度之和。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root):
    """后序遍历计算高度并更新直径。时间 O(n)，空间 O(h)。"""
    max_len = 0

    def depth(node):
        nonlocal max_len
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        max_len = max(max_len, left + right)
        return max(left, right) + 1

    depth(root)
    return max_len


if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert fun(root1) == 3, "示例1失败"
    print("✅ E20 二叉树的直径 全部测试通过")
