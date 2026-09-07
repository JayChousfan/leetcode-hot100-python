"""LeetCode 70. 爬楼梯 (Climbing Stairs) — Hot 100
难度：简单
题目：每次爬 1 或 2 阶，计算爬到第 n 阶的方法数。
示例：n=3 → 3
思路：滚动更新前两个 DP 状态。"""


def fun(n):
    """滚动动态规划。时间 O(n)，空间 O(1)。"""
    prev, cur = 1, 1
    for _ in range(n):
        prev, cur = cur, prev + cur
    return prev


if __name__ == "__main__":
    assert fun(2) == 2, "示例1失败"
    assert fun(3) == 3, "示例2失败"
    print("✅ E04 爬楼梯 全部测试通过")
