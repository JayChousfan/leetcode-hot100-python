"""LeetCode 70. 爬楼梯｜难度：简单
题目：每次爬 1 或 2 阶，计算爬到第 n 阶的方法数。
示例：n=3 → 3
函数：fun(n)"""
# TODO: 在这里写出完整的 def fun(...): 函数
def fun(n):
    prev, cur = 1, 1
    for i in range(n):
        prev, cur = cur, prev + cur
    return prev


if __name__ == "__main__":
    assert fun(2) == 2, "示例1失败"
    assert fun(3) == 3, "示例2失败"
    print("✅ E04 爬楼梯 通过！")
