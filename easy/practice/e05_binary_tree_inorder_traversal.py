"""LeetCode 94. 二叉树的中序遍历｜难度：简单
题目：按“左子树、根节点、右子树”的顺序遍历二叉树。
示例：[1,null,2,3] → [1,3,2]
函数：fun(root)"""
# TODO: 在这里写出完整的 def fun(...): 函数
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root):
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
    assert fun(None) == [], "空树测试失败"
    print("✅ E05 二叉树的中序遍历 通过！")
