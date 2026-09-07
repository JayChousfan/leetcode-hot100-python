"""剑指 Offer JZ8. 二叉树的下一个节点 (Inorder Successor) — 字节真题
难度：中等
题目：节点含父指针，找出它在中序遍历中的下一个节点。
示例：以8为根节点的二叉树中，节点7的中序后继是节点8
思路：有右子树就找右子树最左节点，否则沿父指针向上找。"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def fun(node):
    """根据右子树或父指针寻找后继。时间 O(h)，空间 O(1)。"""
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node is node.parent.right:
        node = node.parent
    return node.parent


if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(6, parent=root)
    root.right = TreeNode(10, parent=root)
    root.left.right = TreeNode(7, parent=root.left)
    root.right.right = TreeNode(11, parent=root.right)
    assert fun(root.left.right) is root, "向上查找测试失败"
    assert fun(root) is root.right, "右子树测试失败"
    assert fun(root.right.right) is None, "无后继测试失败"
    print("✅ P05 二叉树的下一个节点 全部测试通过")
