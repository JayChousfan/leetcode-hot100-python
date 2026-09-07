"""
LeetCode 11. 盛最多水的容器 (Container With Most Water) — ACM 实战
难度：中等

输入：第一行 n，第二行 n 个高度。
输出：容器能够盛水的最大面积。

示例输入：
9
1 8 6 2 5 4 8 3 7

示例输出：
49
"""

import sys


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    height = data[1:1 + n]
    left, right = 0, n - 1
    max_area = 0

    while left < right:
        w = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, w * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    print(max_area)
