"""LeetCode 1. 两数之和｜难度：简单
函数：fun(nums, target) -> list[int]"""
# TODO: 在这里写出完整的 def fun(...): 函数
def fun(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in mp:
            return [mp[complement], i]
        mp[num] = i
    return []

if __name__ == "__main__":
    assert fun([2, 7, 11, 15], 9) == [0, 1], "示例1失败"
    print("✅ E01 两数之和 通过！")
