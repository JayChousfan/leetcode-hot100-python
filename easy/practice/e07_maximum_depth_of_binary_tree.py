"""LeetCode 104. 二叉树的最大深度｜难度：简单
题目：计算二叉树从根节点到最远叶子节点的深度。
示例：[3,9,20,null,null,15,7] → 3
函数：fun(root)"""
# TODO: 在这里写出完整的 def fun(...): 函数
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def fun(root):
    if not root:
        return 0
    return max(fun(root.left),fun(root.right))+1


if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert fun(root1) == 3, "示例1失败"
    assert fun(None) == 0, "空树测试失败"
    print("✅ E07 二叉树的最大深度 通过！")
