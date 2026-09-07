"""
============================================================
LeetCode 62. 不同路径 (Unique Paths) — Hot 100
============================================================
难度：中等

题目：机器人位于 m x n 网格的左上角，每次只能向下或者向右移动一步。
      机器人到达右下角一共有多少条不同的路径？

示例：
  输入: m = 3, n = 7
  输出: 28

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 正确创建二维列表
   C++:  vector<vector<int>> dp(m, vector<int>(n, 0));
   Python: dp = [[0] * n for _ in range(m)]
   → 列表推导式会为每一行创建独立对象

2. 二维列表的引用陷阱
   C++:  每一行 vector 默认独立
   Python: dp = [[0] * n] * m
   → 这种写法让 m 行引用同一个列表，修改 dp[0][0] 会同时改变每一行

3. @lru_cache 递归记忆化
   C++:  用 unordered_map 或二维数组手动缓存递归结果
   Python: @lru_cache(maxsize=None)
   → 装饰器根据函数参数自动缓存返回值，重复状态不会再次计算

4. 装饰器语法
   C++:  没有直接对应语法，通常使用包装函数或模板
   Python: @lru_cache(maxsize=None)
   → @decorator 写在函数上方，相当于用装饰器包装并替换原函数
"""

from functools import lru_cache


def uniquePaths(m: int, n: int) -> int:
    """
    二维动态规划：dp[i][j] 等于上方与左方路径数之和。
    时间复杂度 O(mn)，空间复杂度 O(mn)
    """
    dp = [[0] * n for _ in range(m)]

    # 第一列和第一行都只有一种到达方式
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            # 当前格路径数 = 上方路径数 + 左方路径数
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def uniquePathsMemo(m: int, n: int) -> int:
    """
    使用 @lru_cache 缓存递归状态，作为记忆化搜索写法对照。
    时间复杂度 O(mn)，空间复杂度 O(mn)
    """
    @lru_cache(maxsize=None)
    def paths(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 1
        return paths(i - 1, j) + paths(i, j - 1)

    return paths(m - 1, n - 1)


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = uniquePaths(3, 7)
    assert result1 == 28, f"示例1失败: {result1}"
    assert uniquePaths(3, 2) == 3, "窄网格测试失败"
    assert uniquePaths(1, 1) == 1, "单格网格测试失败"
    assert uniquePathsMemo(3, 7) == 28, "记忆化搜索测试失败"
    print("✅ P14 不同路径 全部测试通过")
