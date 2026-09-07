"""LeetCode 1. 两数之和 (Two Sum) — Hot 100
难度：简单
题目：找出数组中和为 target 的两个数，返回它们的下标。
示例：[2,7,11,15], target=9 → [0,1]
思路：哈希表记录已经出现的数字。"""


def fun(nums, target):
    """一次遍历哈希表。时间 O(n)，空间 O(n)。"""
    mp = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in mp:
            return [mp[complement], i]
        mp[num] = i
    return []


if __name__ == "__main__":
    assert fun([2, 7, 11, 15], 9) == [0, 1], "示例1失败"
    assert fun([3, 3], 6) == [0, 1], "重复元素测试失败"
    print("✅ E01 两数之和 全部测试通过")
