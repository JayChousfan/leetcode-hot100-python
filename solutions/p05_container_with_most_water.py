"""
============================================================
LeetCode 11. 盛最多水的容器 (Container With Most Water) — Hot 100
============================================================
难度：中等

题目：给定长度为 n 的整数数组 height，第 i 条垂线的高度为 height[i]。
      找出两条线，使它们与 x 轴构成的容器可以容纳最多的水。

示例：
  输入: height = [1,8,6,2,5,4,8,3,7]
  输出: 49

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 多变量同时赋值
   C++:  int left = 0, right = height.size() - 1;
   Python: left, right = 0, len(height) - 1
   → Python 会先计算右侧，再把结果分别赋给左侧变量

2. 负数索引
   C++:  height[height.size() - 1]
   Python: height[-1]
   → -1 表示最后一个元素，-2 表示倒数第二个元素

3. min() 决定容器高度
   C++:  min(height[left], height[right])
   Python: min(height[left], height[right])
   → 水面高度由两条边中较短的一条决定

4. 缩进表示代码块
   C++:  if (...) { left++; }
   Python: if ...:
               left += 1
   → Python 不使用大括号，必须保持四个空格缩进
"""


def maxArea(height: list[int]) -> int:
    """
    双指针从两端向中间移动，每次舍弃较短的边以寻找更高边界。
    时间复杂度 O(n)，空间复杂度 O(1)
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        w = right - left
        h = min(height[left], height[right])
        area = w * h
        max_area = max(max_area, area)

        # 移动较短的一侧，才有机会找到更高的边
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "示例1失败"
    assert maxArea([1, 1]) == 1, "双元素测试失败"
    assert maxArea([1, 2, 1]) == 2, "对称高度测试失败"
    print("✅ P05 盛最多水的容器 全部测试通过")
