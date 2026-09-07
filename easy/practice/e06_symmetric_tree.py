"""LeetCode 101. 对称二叉树｜难度：简单
题目：判断一棵二叉树是否左右镜像对称。
示例：[1,2,2,3,4,4,3] → True
函数：fun(root)"""
# TODO: 在这里写出完整的 def fun(...): 函数
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def fun(root):
    def check(left, right):
        if not left or not right:
            return left is right
        return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
    return check(root.left, root.right) if root else True


if __name__ == "__main__":
    assert fun(None), "空树测试失败"
    print("✅ E06 对称二叉树 通过！")
