"""
LeetCode 1. 两数之和 (Two Sum) — ACM 实战
难度：简单

输入：第一行 n 和 target，第二行 n 个整数。
输出：和为 target 的两个元素下标（从 0 开始）。

示例输入：
4 9
2 7 11 15

示例输出：
0 1
"""

import sys


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, target = data[0], data[1]
    nums = data[2:2 + n]
    mp: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in mp:
            print(mp[complement], i)
            break
        mp[num] = i
