"""
LeetCode 283. 移动零 (Move Zeroes) — ACM 实战
难度：简单

输入：第一行 n，第二行 n 个整数。
输出：移动零后的数组，元素用空格分隔。

示例输入：
5
0 1 0 3 12

示例输出：
1 3 12 0 0
"""

import sys


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    nums = data[1:1 + n]
    slow = 0

    for fast in range(n):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    print(*nums)
